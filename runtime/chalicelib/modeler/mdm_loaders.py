import codecs
import hashlib
import json
import os
from collections import OrderedDict, defaultdict
from dataclasses import dataclass
from io import StringIO
from typing import List, Optional, Protocol

import jinja2
import yaml
from loguru import logger

####
gensym_idx = 0


def gensym():
    global gensym_idx
    gensym_idx += 1
    return "_M3_GENSYM_{}".format(gensym_idx)


###


#### jinja extension
class MySQLTriggerExtension(jinja2.ext.Extension):
    tags = frozenset(["trigger"])

    def __init__(self, environment):
        super(MySQLTriggerExtension, self).__init__(environment)
        D = defaultdict(list)
        environment.globals.update(Triggers=D)
        environment.extend(
            install_trigger_globals=self._install,
            triggers=D,
        )

    def _install(self, _globals):
        self.environment.globals.update(**_globals)
        self.environment.extend(**_globals)

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        args = [parser.parse_expression()]
        assert parser.stream.skip_if("comma")
        args.append(parser.parse_expression())
        body = parser.parse_statements(["name:endtrigger"], drop_needle=True)
        return jinja2.nodes.CallBlock(
            self.call_method("_create_trigger", args), [], [], body
        ).set_lineno(lineno)

    def _create_trigger(self, table, mode, caller):
        rv = caller()
        self.environment.triggers[(table, mode)].append(rv)
        return ""


class MySQLSprocExtension(jinja2.ext.Extension):
    tags = frozenset(["sproc"])

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        args = [
            jinja2.nodes.Const(None),
            jinja2.nodes.Const([]),
            jinja2.nodes.Const(False),
        ]
        if parser.stream.current.type != "block_end":
            args[0] = parser.parse_expression()
            if parser.stream.skip_if("comma"):
                args[1] = parser.parse_expression()
            if parser.stream.skip_if("comma"):
                args[2] = parser.parse_expression()

        body = parser.parse_statements(["name:endsproc"], drop_needle=True)
        return jinja2.nodes.CallBlock(
            self.call_method("_create_sproc", args), [], [], body
        ).set_lineno(lineno)

    def _create_sproc(self, name, params, verbose, caller):
        drop = anonymous = autoexec = name is None
        header = footer = ""
        if verbose:
            header = "select 'Executing procedure: {}' as dise_proc_meta;".format(name)
            footer = (
                "select 'Finished executing procedure: {}' as dise_proc_meta;".format(
                    name
                )
            )

        if anonymous and not name:
            name = gensym()
        assert name, name
        return """
delimiter //
drop procedure if exists {name};
create procedure {name}({params})
proc:begin
{header}
{body}
{footer}
end//
delimiter ;
{autoexec}
{drop}
""".format(
            body=caller(),
            header=header,
            footer=footer,
            name=name,
            params=", ".join(params),
            autoexec="call {};".format(name) if autoexec else "",
            drop="drop procedure {};".format(name) if drop else "",
        )


class MySQLFuncExtension(jinja2.ext.Extension):
    tags = frozenset(["func"])

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        args = [
            jinja2.nodes.Const(None),
            jinja2.nodes.Const([]),
            jinja2.nodes.Const([]),
        ]
        if parser.stream.current.type != "block_end":
            args[0] = parser.parse_expression()
            if parser.stream.skip_if("comma"):
                args[1] = parser.parse_expression()
            if parser.stream.skip_if("comma"):
                args[2] = parser.parse_expression()

        body = parser.parse_statements(["name:endfunc"], drop_needle=True)
        return jinja2.nodes.CallBlock(
            self.call_method("_create_func", args), [], [], body
        ).set_lineno(lineno)

    def _create_func(self, name, params, modifiers, caller):
        assert name, name
        return """
delimiter //
drop function if exists {name};
create function {name}({params})
{modifiers}
begin
{body}
end//
delimiter ;
""".format(
            body=caller(),
            name=name,
            modifiers="\n".join(modifiers),
            params=", ".join(params),
        )


####
@dataclass
class EnvLoader(Protocol):
    env: jinja2.Environment = None
    env_text: jinja2.Environment = None

    def create_env(file_loader=True):
        # bcc = jinja2.FileSystemBytecodeCache(CACHE_DIR, "%s.cache")
        if file_loader:
            env = jinja2.Environment(
                loader=jinja2.ChoiceLoader(
                    [
                        jinja2.FileSystemLoader("."),
                        jinja2.FileSystemLoader(
                            os.environ.get("DISEGEN_BASE", "disegen")
                        ),
                        jinja2.FunctionLoader(
                            lambda f: codecs.open(f, "r", "utf-8").read()
                        ),
                    ]
                ),
                undefined=jinja2.StrictUndefined,
                extensions=[
                    MySQLTriggerExtension,
                    MySQLSprocExtension,
                    MySQLFuncExtension,
                    "jinja2.ext.do",
                ],
                # Disable bytecode cache due to sporadic mysterious errors from custom
                # extensions:
                # bytecode_cache=bcc,
            )
        else:
            env = jinja2.Environment(
                loader=jinja2.FunctionLoader(lambda x: x),
                undefined=jinja2.StrictUndefined,
                extensions=[
                    MySQLTriggerExtension,
                    MySQLSprocExtension,
                    MySQLFuncExtension,
                    "jinja2.ext.do",
                ],
                # Disable bytecode cache due to sporadic mysterious errors from custom
                # extensions:
                # bytecode_cache=bcc,
            )

        def uniq(seq):
            seen = set()
            return [x for x in seq if x not in seen and not seen.add(x)]

        env.filters["uniq"] = uniq

        # load host env vars into jinja2 environment
        env.globals.update(get_host_env=lambda key: os.getenv(key))
        logger.debug(env)
        return env


### yaml loader


class OrderedJsonEncoder(json.JSONEncoder):
    def encode(self, o):
        if isinstance(o, OrderedDict):
            return "{%s}" % ",".join(
                "%s:%s" % (self.encode(str(k)), self.encode(v)) for k, v in o.items()
            )
        else:
            return json.JSONEncoder.encode(self, o)


json_encoder = OrderedJsonEncoder()
json_load = json.load
json_loads = json.loads

CACHE_DIR = "{}/.cache/{}".format(os.environ["HOME"], "m3")
if not os.path.exists(CACHE_DIR):
    os.mkdir(CACHE_DIR)


def yaml_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    "Ordered YAML loader"

    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping,
    )

    s = StringIO(stream.read())
    sha256 = hashlib.sha256(s.getvalue().encode("utf-8")).hexdigest()
    cache_path = "{}/{}.json".format(CACHE_DIR, sha256)
    if os.path.exists(cache_path):
        return json_load(open(cache_path, "r"))
    else:
        obj = yaml.load(s, OrderedLoader)
        with open(cache_path + ".tmp", "w") as fh:
            fh.write(json_encoder.encode(obj))
        os.rename(cache_path + ".tmp", cache_path)
        return obj
