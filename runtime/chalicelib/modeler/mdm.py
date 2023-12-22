#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import hashlib
import json
import os
import re
import sys
from collections import OrderedDict, defaultdict, namedtuple
from functools import wraps
from io import StringIO
from itertools import chain
from pdb import set_trace
from pprint import pformat

import jinja2
import jinja2.ext
import yaml

json_load = json.load
json_loads = json.loads
from icecream import ic
from loguru import logger

logger.info("asdad")

try:
    basestring
except NameError:
    basestring = str


from .mdm_loaders import EnvLoader, yaml_load

##### schemas.py
from .schemas import (
    Backref,
    BlockElement,
    ForeignKey,
    InverseForeignKey,
    LogicalColumn,
    LogicalEnum,
    LogicalTable,
    LogicalTie,
    SystemDefinition,
    TableTieRelation,
    VirtualAttribute,
)


class attrdict(dict):
    def __getattr__(self, key):
        return self[key]


class attr_defaultdict(defaultdict):
    def __getattr__(self, key):
        return self[key]


Tags = attr_defaultdict(OrderedDict)
mdm_attributes = {}
# mdm_csv_path = "{}/mdm.csv".format(os.path.dirname(__file__))

# gensym_idx = 0


# def gensym():
#     global gensym_idx
#     gensym_idx += 1
#     return "_M3_GENSYM_{}".format(gensym_idx)


# Backref = namedtuple("Backref", "attribute ref_table ref_id ref_type")


def get_backref(table, colname, block):
    "Hacky workaround for backrefs (for now)"
    assert re.search("^(backref|custom)", block.value), (table.name, colname, block)
    ref_type, ref_table, ref_id = re.findall(
        "(backref|custom view) (.+)\((.+)\)", block.value
    )[0]
    return Backref(colname, ref_table, ref_id, ref_type)


def get_globals():
    G = dict(
        map=map,
        mdm_attributes=mdm_attributes,
        Tags=Tags,
        fk_name=fk_name,
        table_name=table_name,
        log_table_name=log_table_name,
        mysql_type=mysql_type,
        # java_type=java_type,
        column_maxsize=column_maxsize,
        python_class_name=python_class_name,
        java_class_name=java_class_name,
        java_enum_code=java_enum_code,
        camel_case=camel_case,
        tie_other=tie_other,
        Tables=Tables,
        Ties=Ties,
        Enums=Enums,
        dTables=dTables,
        dTableFields=dTableFields,
        dTableTies=dTableTies,
        dEnums=dEnums,
        dEnumCodes=dEnumCodes,
        dTies=dTies,
        dColumns=dColumns,
        dColumnAliases=dColumnAliases,
        sorted=sorted,
        set=set,
        pformat=pformat,
        # gensym=gensym,
        get_backref=get_backref,
        Systems=Systems,
        environ=attr_defaultdict(lambda: None, os.environ),
    )

    def _assert(x, y=None):
        print(x)
        print(y)
        assert x
        assert y

    G["do_assert"] = _assert

    for k, v in os.environ.items():
        if k in G:
            ## logger.debug("Warning: skipping overlapping env var:", k, file=sys.stderr)
            continue
        G[k] = v

    G["DEBUG"] = G.get("DEBUG", False)
    return G


def setup_globals():
    # Remove overridden Enums:
    Enums[:] = sorted(
        (
            x
            for i, x in enumerate(Enums)
            if i == max(j for j, z in enumerate(Enums) if x.name == z.name)
        ),
        key=lambda x: x.name,
    )
    # Remove overridden Tables:
    Tables[:] = sorted(
        (
            x
            for i, x in enumerate(Tables)
            if i == max(j for j, z in enumerate(Tables) if x.name == z.name)
        ),
        key=lambda x: x.name,
    )

    global dTables, dEnums, dEnumCodes, dTies, dTableTies, dColumns, dColumnAliases
    dTables = attrdict({table.name: table for table in Tables})
    dEnums = attrdict({enum.name: enum for enum in Enums})
    dEnumCodes = attrdict(
        {enum.name: attrdict((v, k) for k, v in enum.values.items()) for enum in Enums}
    )
    dTies = attrdict({tie.name: tie for tie in Ties})
    dTableTies = attrdict(
        {table.name: frozenset(t.relation_name for t in table.ties) for table in Tables}
    )
    dColumns = attrdict(
        {
            table.name: attrdict({col.name: col for col in table.all_columns})
            for table in Tables
        }
    )

    # db_name aliases:
    for table in Tables:
        dColumns[table.name].update({col.db_name: col for col in table.all_columns})

    # Hack for irregular naming:
    # mdm_attributes['E_person'] = mdm_attributes['E_external_person']


def eval_template(path, **kw):
    return env.get_template(path).render(
        **kw
    )  # , globals=get_globals()).render(**get_globals())


def eval_template_text(text, path, **kw):
    x = env_text.get_template(text, globals=get_globals()).render(**kw)
    assert (
        x is not None and x.strip() != ""
    ), "Template {} evaluated to nothing!".format(path)
    return x


def mysql_type(col):
    type_ = dict(bool="char(1)", timestamptz="datetime").get(col.type, col.type)

    if "MYSQL_TYPE" in col.tags:
        return col.tags.MYSQL_TYPE

    # backwards compatibility hack:
    if "serial" in type_:
        return type_.replace("serial", "int") + " auto_increment"

    type_ = "bigint" if col.fk and col.type == "int" else type_
    if col.name == "id" and col.pk:
        return "bigint"

    return type_


def column_maxsize(col, fallback):
    if col.type in "text varchar".split():
        return int(1e6)
    elif "(" in col.type:
        return int(col.type[1 + col.type.find("(") : -1])
    else:
        return fallback


def python_class_name(name):
    return Tags.PYCLASS.get(name, camel_case(name))


def unaccent(x):
    return (
        x.replace("ä", "a")
        .replace("Ä", "A")
        .replace("ö", "o")
        .replace("Ö", "O")
        .replace("å", "a")
        .replace("å", "a")
    )


re_java_enum = re.compile("[^\w_]")


def java_enum_code(code):
    x = "".join(
        x[0].upper() + x[1:] if x else "" for x in re_java_enum.split(unaccent(code))
    )
    if re.search("^[0-9]", x):
        return "_" + x
    else:
        return x


def java_class_name(name, full=False):
    name2 = name[2:] if re.search("^[A-Z]_", name) else name
    x = Tags.CLASS.get(name, camel_case(name2))
    if full and "." not in x:
        return "fi.dise.model.{}".format(x)
    else:
        return x


def camel_case(name):
    return "".join(x[0].upper() + x[1:] if x else "" for x in name.split("_"))


def table_name(table, sim=True):
    # Non-capitalized tables like d_person_permissions are meant to be named as such:
    if table[0].islower():
        return table

    if sim and table in Tags.SIMULATED:
        table = "O_{0}".format(table)
    return table.upper()


def log_table_name(table, suffix="LOG"):
    # x = 'E_person' if table == 'E_external_person' else table
    return "{}_{}".format(x.upper(), suffix)


def fk_name(table, col):
    x = "fk_{}_{}".format(table.name, col)
    if len(x) > 63:
        hash_ = hashlib.sha256((table.name + col).encode("utf8")).hexdigest()[:8]
        x = "fk_{}_{}_{}".format(table.name[:16], col[:16], hash_)
    return x


def get_column_blocks(cols):
    if isinstance(cols, basestring):
        return BlockElement(value=cols, type="string")
    assert isinstance(cols, list), cols
    d = OrderedDict()
    for col in cols:
        assert isinstance(col, dict), repr(col)
        meta_excluded = list((k, v) for k, v in col.items() if k != "TAGS")
        assert len(meta_excluded) == 1, meta_excluded
        name, value = meta_excluded[0]
        d[name] = get_column_blocks(value)
    return BlockElement(value=d, type="block")


# LogicalTable = namedtuple(
#     "LogicalTable",
#     """
# name localized id_type inverse_fks valid_type internal historized pk attributes all_columns
# old_audit ties blocks field_blocks tags
# backrefs
# virtual_attributes
# indexes
# unique_indexes
# """,
# )

# LogicalColumn = namedtuple(
#     "LogicalColumn",
#     """
# name db_name default localized valid_type type serial_type nullable fk unique pk enum tags
# """,
# )
# LogicalTie = namedtuple("LogicalTie", "name valid_type fks")
# TableTieRelation = namedtuple("TableTieRelation", "name relation_name other")
# LogicalEnum = namedtuple(
#     "LogicalEnum", "name id_type valid_type coded localized values values_localized"
# )
# ForeignKey = namedtuple("ForeignKey", "table ref_id name")
# InverseForeignKey = namedtuple("InverseForeignKey", "table valid_type name")
# BlockElement = namedtuple("BlockElement", "value type")
# VirtualAttribute = namedtuple("VirtualAttribute", "name type")

# SystemDefinition = namedtuple("SystemDefinition", "attributes aces global_aces")


Tables = []
Enums = []
Ties = []
dTables = {}
dEnums = {}
dEnumCodes = {}
dTies = {}
dColumns = {}
dTableTies = {}
dTableFields = {}
_Backrefs = defaultdict(list)

dColumnAliases = defaultdict(dict)
"{ table name -> { alias : column name } }"

gColumnAliases = {}
"{ alias : column name }"
gTableAliases = {}
"{ table name : new name }"

Systems = {}
"{ system identifier : (system with associated ACEs) }"


def tie_other(tie, table):
    assert isinstance(table, basestring), table
    return next(fk.table for fk in dTies[tie].fks if fk.table != table)


class LazyTieRelation(object):
    def __init__(self, tie, table):
        self.tie, self.table = tie, table

    def __repr__(self):
        return next(x.table for x in dTies[self.tie].fks if x.table != self.table)


class LazyFKType(object):
    def __init__(self, fk):
        self.fk = fk

    def __repr__(self):
        "Warning: Hacks ahead"
        if self.fk.ref_id == "id":
            return "int"
        for table in Tables:
            if table.name != self.fk.table:
                continue
            for col in table.pk:
                if col.name == self.fk.ref_id:
                    return col.type

        assert False, "Could not find FK reference: {}".format(self.fk)


class LazyInverseFKs(object):
    def __init__(self, table):
        self.table = table

    def __iter__(self):
        for table in Tables:
            for col in table.all_columns:
                if col.fk and col.fk.table == self.table:
                    assert col.fk.ref_id == "id"
                    yield InverseForeignKey(
                        table=table.name,
                        name=col.fk.name,
                        valid_type=col.valid_type,
                    )


def verify_ace(ace):
    assert isinstance(ace, dict), ace
    assert "ace_types" in ace, ace
    assert "name" in ace, ace
    assert "value" in ace, ace


def ace_load(kv):
    system_definition = dict(kv)
    system_attributes = system_definition["System"]
    sys_id = system_attributes["identifier"]
    system = Systems[sys_id] = SystemDefinition(
        attributes=system_attributes,
        aces=system_definition.get("Aces", ()),
        global_aces=system_definition.get("GlobalAces", ()),
    )

    for ace in system.aces:
        verify_ace(ace)
    for ace in system.global_aces:
        verify_ace(ace)


def parse_tags_block(tags):
    "<TAGS> -> [ (tag name, value(s)) ]"
    assert isinstance(tags, list), repr(tags)
    for tagp in tags:
        tag, params = tagp.split("(", 1) if "(" in tagp else (tagp, "")
        params = params.split(")", 1)[0].split(",")
        yield tag, params[0] if len(params) == 1 else params


def m3_load_iter(it):
    for table, _cols in it:
        ic(table)
        ic(_cols)

        m3_load(table, _cols)


def m3_load(table, _cols):
    if table == "COLUMN_RENAMES":
        global gColumnAliases
        gColumnAliases = _cols
        # print (_cols, file=sys.stderr)
        return

    if table == "TABLE_RENAMES":
        global gTableAliases
        gTableAliases = _cols
        # print (_cols, file=sys.stderr)
        return

    cols = _cols.get("ATTRIBUTES", [])

    valid_type = "tstzrange"
    table_tags = attrdict(parse_tags_block(_cols.get("TAGS", [])))

    _aliases = _cols.get("COLUMN_ALIASES")
    if _aliases:
        # dColumnAliases[table] = dict(gColumnAliases) #?
        dColumnAliases[table] = {v: k for k, v in _aliases.items()}

    for tag, val in table_tags.items():
        Tags[tag][table] = val

    _columns = []

    if "ENUM" in table_tags:
        id_type_ = [x for x in cols if "type" in x]
        id_type = id_type_[0]["type"] if id_type_ else "smallint"

        values_localized = {}
        for attr, value in _cols.items():
            if not attr.startswith("values"):
                continue
            lang = re.findall("values\((.*)\)", attr)
            type_ = int if id_type.endswith("int") else str
            assert value is not None, (attr, value, cols)
            values_localized[lang[0] if lang else None] = {
                type_(k): v for k, v in value.items()
            }

        assert len(values_localized) > 0, table

        if None in values_localized:
            values = values_localized[None]
            del values_localized[None]
        else:
            values = values_localized.get("en") or values_localized["fi"]

        values = {k: java_enum_code(v) for k, v in values.items()}

        Enums.append(
            LogicalEnum(
                name=table,
                id_type=id_type,
                valid_type=valid_type,
                values=values,
                values_localized=values_localized,
                coded=True,  # has a canonical code name? (non-localized)
                localized="LOCALIZED" in table_tags,
            )
        )
        return

    if "TIE" in table_tags:
        columns = []
        fks = []
        for col in cols:
            name, fk_text = list(col.items())[0]
            if name == "OLD":  # Datamaster specific atm
                continue

            if name == "valid":
                valid_type = fk_text
                continue
            r = re.findall("^references (.*)\((.*)\)", fk_text)
            assert r, fk_text
            _table, ref_id = r[0]
            fks.append(ForeignKey(_table, ref_id, name))

        Ties.append(
            LogicalTie(
                name=table,
                valid_type=valid_type,
                fks=fks,
            )
        )
        return

    backrefs = []
    table_localized = False
    pk = []
    pk_col_names = _cols.get("primary key", "").split(", ")
    col_names = set()
    tie_relations = []

    blocks = get_column_blocks(cols)
    field_blocks = blocks

    if table in dTableFields:
        field_blocks = merge_field_blocks(table, blocks, dTableFields[table])

    indexes = _cols.get("INDEXES", {})
    unique_indexes = _cols.get("UNIQUE INDEXES", {})
    virtual_attributes = [
        VirtualAttribute(
            name=list(d.items())[0][0],
            type=list(d.items())[0][1],
        )
        for d in _cols.get("VIRTUAL ATTRIBUTES", [])
    ]

    # XXX: cheap hack since I can't be bothered to migrate to this properly yet in ddl/*.yaml*
    if "API" in _cols.get("TAGS", []) and "deleted" in cols:
        virtual_attributes.append(VirtualAttribute(name="valid", type="bool"))
    virtual_attributes = [
        LogicalColumn(
            name=attr.name,
            db_name=attr.name,
            default=None,
            valid_type=None,
            type=attr.type,
            enum=None,
            serial_type=None,
            nullable=False,
            fk=None,
            unique=False,
            pk=False,
            localized=False,  # ?
            tags=[],
        )
        for attr in virtual_attributes
    ]

    assert isinstance(indexes, dict)
    assert isinstance(unique_indexes, dict)
    assert isinstance(virtual_attributes, list)

    while cols:
        col = cols.pop(0)
        dd = {}

        c_tags_str = col.pop("TAGS") if "TAGS" in col else []
        c_tags = attrdict(parse_tags_block(c_tags_str))

        assert len(col) == 1, repr(col)
        col_name, col_attrs = list(col.items())[0]

        if isinstance(col_attrs, list):
            cols[:] = col_attrs + cols
            continue

        assert " " not in col_name, col
        assert isinstance(col_attrs, basestring), col

        r = re.findall("^references (.*)\((.*)\)(\s+<-> .*)?", col_attrs)

        dd["enum"] = dd["fk"] = None
        if col_attrs.startswith("enum"):
            _keyword, enum_name = col_attrs.split()[:2]
            dd["type"] = "int"  # for now...
            dd["enum"] = enum_name

        elif r:
            _table, ref_id, backref = r[0]
            dd["fk"] = ForeignKey(_table, ref_id, col_name)
            dd["type"] = repr(LazyFKType(dd["fk"]))
            assert isinstance(dd["type"], basestring), dd

            # XXX: major hack to work around the hack that is LazyFKType.
            if dd["type"] == "int":
                dd["type"] = "bigint"

            # if backref or table in Tags.BACKREF:
            #     _Backrefs[table].append(dd)

        else:
            dd["type"] = col_attrs.split()[0]

        # TODO:
        if dd["type"] == "tie":
            tie_name = col_attrs.split()[-1]
            tie_relations.append(
                TableTieRelation(
                    name=tie_name,
                    relation_name=col_name,
                    other=LazyTieRelation(tie_name, table),
                )
            )
            continue

        dd["name"] = dd["db_name"] = col_name
        dd["serial_type"] = dd["type"]
        dd["nullable"] = re.search(r"\brequired\b", col_attrs) is None
        dd["valid_type"] = valid_type  # TODO: support attribute-level exceptions
        dd["unique"] = re.search(r"\bunique\b", col_attrs) is not None
        dd["pk"] = (
            re.search(r"\bprimary key\b", col_attrs) is not None
            or col_name in pk_col_names
        )
        dd["localized"] = re.search(r"\blocalized\b", col_attrs) is not None
        table_localized = table_localized or dd["localized"]

        col_attrs_ = col_attrs.split()
        if "default" in col_attrs_:
            dd["default"] = col_attrs_[1 + col_attrs_.index("default")]
        else:
            dd["default"] = None

        if dd["type"] == "backref":
            ref_table, ref_id = re.findall("backref (.+)\((.+)\)", col_attrs)[0]
            backrefs.append(Backref(col_name, ref_table, ref_id, "backref"))
            continue
        if dd["type"] == "custom":
            ref_table, ref_id = re.findall("custom view (.+)\((.+)\)", col_attrs)[0]
            # backrefs.append(Backref(attr_name, ref_table, ref_id, 'custom view'))
            continue

        ## Column renames:
        # Avoid reserved keywords and such:
        if dd["name"] == "public":
            dd["name"] = dd["name"] + "_"

        dd["tags"] = c_tags
        col = LogicalColumn(**dd)
        if dd["pk"]:
            pk.append(col)
        else:
            _columns.append(col)

        # Column names must be unique:
        assert col.name not in col_names, "Duplicate column for table {}: {}".format(
            table, col.name
        )

        col_names.add(col.name)

    if len(pk) == 0 and table not in Tags.NO_PK:
        pk.append(
            LogicalColumn(
                name="id",
                db_name="id",
                default=None,
                valid_type="tstzrange",  # ?
                type="int",
                enum=None,
                serial_type="serial",
                nullable=False,
                fk=None,
                unique=True,
                pk=True,
                localized=False,  # ?
                tags=[],
            )
        )

    if table in Tags.MATERIALIZED_STATE:
        assert pk[-1].type == "timestamptz", "Materialized state views must have "
        "timestamp column as the last column: {} / {}".format(
            table, ", ".join(x.name for x in pk)
        )

    assert len(pk) > 0 or table in Tags.NO_PK
    id_type = tuple(x.type for x in pk)
    assert table not in [t.name for t in Tables], table
    new_logical_table = LogicalTable(
        name=table,
        id_type=id_type,
        historized=table in Tags.HISTORIZED,
        internal="INTERNAL" in table_tags,
        valid_type=valid_type,
        pk=pk,
        inverse_fks=LazyInverseFKs(table),
        attributes=_columns,
        all_columns=list(chain(pk, _columns)),
        localized=table_localized,
        indexes=indexes,
        unique_indexes=unique_indexes,
        old_audit="{}_A".format(table_name(table, sim=False))
        if table in Tags.HISTORIZED and table not in Tags.NO_AUDIT
        else None,
        ties=tie_relations,
        blocks=blocks,
        field_blocks=field_blocks,
        tags=table_tags,
        backrefs=backrefs,
        virtual_attributes=virtual_attributes,
    )
    pformat(new_logical_table)
    # set_trace()
    print("asdasd")
    # logical_table = LogicalTable(
    #     name=table,
    #     id_type=id_type,
    #     historized=table in Tags.HISTORIZED,
    #     internal="INTERNAL" in table_tags,
    #     valid_type=valid_type,
    #     pk=pk,
    #     inverse_fks=LazyInverseFKs(table),
    #     attributes=_columns,
    #     all_columns=list(chain(pk, _columns)),
    #     localized=table_localized,
    #     indexes=indexes,
    #     unique_indexes=unique_indexes,
    #     old_audit="{}_A".format(table_name(table, sim=False))
    #     if table in Tags.HISTORIZED and table not in Tags.NO_AUDIT
    #     else None,
    #     ties=tie_relations,
    #     blocks=blocks,
    #     field_blocks=field_blocks,
    #     tags=table_tags,
    #     backrefs=backrefs,
    #     virtual_attributes=virtual_attributes,
    # )
    Tables.append(new_logical_table)

    # def create_env(file_loader=True):
    #     bcc = jinja2.FileSystemBytecodeCache(CACHE_DIR, "%s.cache")
    #     env = jinja2.Environment(
    #         loader=jinja2.ChoiceLoader(
    #             [
    #                 jinja2.FileSystemLoader("."),
    #                 jinja2.FileSystemLoader(os.environ.get("DISEGEN_BASE", "disegen")),
    #                 jinja2.FunctionLoader(lambda f: codecs.open(f, "r", "utf-8").read()),
    #             ]
    #         )
    #         if file_loader
    #         else jinja2.FunctionLoader(lambda x: x),
    #         undefined=jinja2.StrictUndefined,
    #         extensions=[
    #             MySQLTriggerExtension,
    #             MySQLSprocExtension,
    #             MySQLFuncExtension,
    #             "jinja2.ext.do",
    #         ],
    #         # Disable bytecode cache due to sporadic mysterious errors from custom
    #         # extensions:
    #         # bytecode_cache=bcc,
    #     )

    #     def uniq(seq):
    #         seen = set()
    #         return [x for x in seq if x not in seen and not seen.add(x)]

    #     env.filters["uniq"] = uniq

    # load host env vars into jinja2 environment
    env.globals.update(get_host_env=lambda key: os.getenv(key))
    ## logger.debug(env)
    return env


def load_defs(dir_, load_fn):
    files = sorted(os.listdir(dir_))
    PATH = ["{}/{}".format(dir_, x) for x in files if x.endswith(".yaml")]
    PATH_jinja2 = ["{}/{}".format(dir_, x) for x in files if x.endswith(".yaml.jinja2")]
    ic(PATH)
    ic(PATH_jinja2)
    for f in PATH:
        if os.environ.get("DEBUG"):
            logger.debug("Processing file: {}".format(f), file=sys.stderr)
        d = codecs.open(f, "r", "utf-8")
        x = yaml_load(d)
        assert x, "File does not have any valid definitions: {}".format(f)
        load_fn(x.items())

    for path in PATH_jinja2:
        if os.environ.get("DEBUG"):
            logger.debug("Processing file: {}".format(path), file=sys.stderr)
        d = eval_template_text(codecs.open(path, "r", "utf-8").read(), path=path)
        load_fn(yaml_load(StringIO(d)).items())


def flatten_blocks(blocks):
    for c, b in blocks.value.items():
        if b.type == "string":
            yield c, b
        else:
            for x in flatten_blocks(b):
                yield x


def merge_field_blocks(table, blocks, fields, flat=None):
    flat = flat or dict(flatten_blocks(blocks))
    d = OrderedDict()
    for c, b in fields.value.items():
        if b is None:
            assert (
                c in flat
            ), "Unknown column referenced in field definition for {}: {}".format(
                table, c
            )
            d[c] = flat[c]
            assert flat[c].type == "string", flat[c]
        elif b.type == "block":
            d[c] = merge_field_blocks(table, blocks, b, flat)
        else:
            d[c] = b

    return BlockElement(value=d, type="block")


def get_column_blocks_ui(cols):
    if isinstance(cols, basestring):
        return BlockElement(value=cols, type="string")
    assert isinstance(cols, list), cols
    d = OrderedDict()
    for col in cols:
        if isinstance(col, dict):
            name, value = list(col.items())[0]
            d[name] = get_column_blocks_ui(value)
        else:
            d[col] = None
    return BlockElement(value=d, type="block")


def load_fields(f):
    d = codecs.open(f, "r", "utf-8")
    for table, cols in yaml_load(d).items():
        yield table, get_column_blocks_ui(cols)


def sanity_checks():
    # Some sanity checks before printing anything:
    for table in Tables:
        for col in table.all_columns:
            if col.enum:
                # assert col.enum in dEnums, col.enum
                if col.enum not in dEnums:
                    ic("Missing enum:", table.name, col.name, col.enum, file=sys.stderr)

    for table in Tables:
        for col in table.pk:
            assert col.pk, (table, col)
        for col in table.attributes:
            assert not col.pk, (table, col)
            if col.enum and col.default is not None:
                assert (
                    col.default in dEnumCodes[col.enum]
                ), "Enum column default value must be a symbol: {}".format(col)

    TABLES = frozenset(t.name for t in Tables)
    for (table, mode), code in list(env.triggers.items()):
        assert table in TABLES, (table, mode)
        assert mode[0] in "BA" and mode[1] in "IU", (table, mode)


def main(
    # argv=[
    #     ""
    # ],
    input_dirs=["chalicelib/static"],
    input_templates=["chalicelib/templates/models.py.jinja2"],
    kwarg={},
):
    """
    This function to generate code from template and definition from yaml
    - open mdm.csv ? why
    - load fields.yaml , this is listed fields to be showed based on customer
    - load enum and ddl then load definitions with load_defs(path , m3_load_iter )
    """
    # for line in codecs.open(mdm_csv_path, "r", "utf-8").read().splitlines():
    #     table, attr = line.split(",", 1)
    #     # ## logger.debug( table, attr)
    #     if not table in mdm_attributes:
    #         mdm_attributes[table] = []
    #     mdm_attributes[table].append(attr)

    # input_dirs = argv[0 : argv.index("--")] if "--" in argv else "chalicelib/modeler/static"
    # input_templates = argv[argv.index("--") + 1 :] if "--" in argv else []
    ## logger.debug(input_dirs)
    ## logger.debug(input_templates)
    # Load ddl/, fields.yaml
    for dir_ in input_dirs:
        fields_yaml = os.path.join(dir_, "fields.yaml")
        if os.path.exists(fields_yaml):
            dTableFields.update(load_fields(fields_yaml))

    for dir_ in input_dirs:
        for x in ("enums", "ddl"):
            path = os.path.join(dir_, x)
            if not os.path.exists(path):
                continue
            ## logger.debug(path)
            load_defs(path, m3_load_iter)

    assert Tables, "No table definitions loaded"

    setup_globals()
    env.install_trigger_globals(get_globals())

    # ACE definitions
    for dir_ in input_dirs:
        path = os.path.join(dir_, "aces")
        if not os.path.exists(path):
            continue
        load_defs(path, ace_load)

    for dir_ in input_dirs:
        triggers = os.path.join(dir_, "triggers")
        if os.path.exists(triggers):
            for p in os.listdir(triggers):
                if ".appledouble" in p.lower():
                    continue
                eval_template(os.path.join(triggers, p))

    re_trailing_space = re.compile(" +$", re.MULTILINE)
    re_lines = re.compile("\n+$", re.MULTILINE)
    stdout = ""
    res = str()
    for path in input_templates:
        paths = path.split("=", 1)
        path_in, path_out = paths if paths[1:] else (path, None)
        path_out = "test.py"
        if os.environ.get("DEBUG"):
            logger.debug("Evaluating template: {}".format(path_in), file=sys.stderr)

        out = re_lines.sub("\n", re_trailing_space.sub("", eval_template(path_in)))
        ic(path_out)
        if path_out:
            with codecs.open(path_out, "wb", "utf-8") as fh:
                logger.debug(out, file=fh)
        else:
            stdout += out
            res += out

    sanity_checks()
    return res


env = EnvLoader.create_env()
env_text = EnvLoader.create_env(file_loader=False)

if __name__ == "__main__":
    """
    1. Input :
    - input_dir : This is directroty store yaml files
    - input_templates: templates
    2. Output : text
    """
    logger.info(sys.argv)
    # main(sys.argv)
