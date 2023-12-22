_java_types = dict(
    bool="boolean",
    int="int",
    bigint="long",
    smallint="int",
    serial="int",
    bigserial="bigint",
    date="Date",
    timestamptz="Date",
    real="double",
    bytea="byte[]",
)


def java_type(col):
    if col.fk:
        return "long"

    elif (
        col.type.startswith("varchar")
        or col.type.startswith("char")
        or col.type.endswith("text")
    ):
        return "String"

    return _java_types[col.type]
