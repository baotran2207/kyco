import os
import re
from collections import OrderedDict, defaultdict
from pprint import pformat

from .schemas import Backref, LogicalEnum, LogicalTable, LogicalTie


class attrdict(dict):
    def __getattr__(self, key):
        return self[key]


class attr_defaultdict(defaultdict):
    def __getattr__(self, key):
        return self[key]


Tables: [LogicalTable] = []
Enums: [LogicalEnum] = []
Ties: [LogicalTie] = []
dTables = {}
dEnums = {}
dEnumCodes = {}
dTies = {}
dColumns = {}
dTableTies = {}
dTableFields = {}
_Backrefs = defaultdict(list)

mdm_attributes = {}
Tags = attr_defaultdict(OrderedDict)


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
        java_type=java_type,
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
        gensym=gensym,
        get_backref=get_backref,
        Systems=Systems,
        environ=attr_defaultdict(lambda: None, os.environ),
    )

    def _assert(x, y=None):
        assert x, y

    G["assert"] = _assert

    for k, v in os.environ.items():
        if k in G:
            # logger.debug('Warning: skipping overlapping env var:', k, file=sys.stderr)
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
