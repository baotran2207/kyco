import datetime
from collections import defaultdict, deque
from decimal import Decimal
from enum import Enum

# from ipaddress import (
#     IPv4Address,
#     IPv4Interface,
#     IPv4Network,
#     IPv6Address,
#     IPv6Interface,
#     IPv6Network,
# )
from pathlib import Path, PurePath
from re import Pattern
from types import GeneratorType

# from types import GeneratorType
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Type, Union
from uuid import UUID

from pydantic import BaseModel
from pydantic.color import Color
from pydantic.networks import AnyUrl, NameEmail
from pydantic.types import SecretBytes, SecretStr

# from typing_extensions import Annotated, Doc  # type: ignore [attr-defined]


# Taken from Pydantic v1 as is
# TODO: pv2 should this return strings instead?
def isoformat(o: Union[datetime.date, datetime.time]) -> str:
    return o.isoformat()


# Taken from Pydantic v1 as is
# TODO: pv2 should this return strings instead?
def decimal_encoder(dec_value: Decimal) -> Union[int, float]:
    """
    Encodes a Decimal as int of there's no exponent, otherwise float

    This is useful when we use ConstrainedDecimal to represent Numeric(x,0)
    where a integer (but not int typed) is used. Encoding this as a float
    results in failed round-tripping between encode and parse.
    Our Id type is a prime example of this.

    >>> decimal_encoder(Decimal("1.0"))
    1.0

    >>> decimal_encoder(Decimal("1"))
    1
    """
    if dec_value.as_tuple().exponent >= 0:  # type: ignore[operator]
        return int(dec_value)
    else:
        return float(dec_value)


ENCODERS_BY_TYPE: Dict[Type[Any], Callable[[Any], Any]] = {
    bytes: lambda o: o.decode(),
    Color: str,
    datetime.date: isoformat,
    datetime.datetime: isoformat,
    datetime.time: isoformat,
    datetime.timedelta: lambda td: td.total_seconds(),
    Decimal: decimal_encoder,
    Enum: lambda o: o.value,
    frozenset: list,
    deque: list,
    GeneratorType: list,
    # IPv4Address: str,
    # IPv4Interface: str,
    # IPv4Network: str,
    # IPv6Address: str,
    # IPv6Interface: str,
    # IPv6Network: str,
    NameEmail: str,
    Path: str,
    Pattern: lambda o: o.pattern,
    SecretBytes: str,
    SecretStr: str,
    set: list,
    UUID: str,
    # Url: str,
    AnyUrl: str,
}


SetIntStr = Set[Union[int, str]]
DictIntStrAny = Dict[Union[int, str], Any]


def generate_encoders_by_class_tuples(
    type_encoder_map: Dict[Any, Callable[[Any], Any]]
) -> Dict[Callable[[Any], Any], Tuple[Any, ...]]:
    encoders_by_class_tuples: Dict[Callable[[Any], Any], Tuple[Any, ...]] = defaultdict(
        tuple
    )
    for type_, encoder in type_encoder_map.items():
        encoders_by_class_tuples[encoder] += (type_,)
    return encoders_by_class_tuples


encoders_by_class_tuples = generate_encoders_by_class_tuples(ENCODERS_BY_TYPE)


def jsonable_encoder(
    obj: Any,
    include: Optional[Union[SetIntStr, DictIntStrAny]] = None,
    exclude: Optional[Union[SetIntStr, DictIntStrAny]] = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    custom_encoder: Dict[Any, Callable[[Any], Any]] = {},
    sqlalchemy_safe: bool = True,
) -> Any:
    if include is not None and not isinstance(include, set):
        include = set(include)
    if exclude is not None and not isinstance(exclude, set):
        exclude = set(exclude)
    if isinstance(obj, BaseModel):
        return _encode_base_model(
            obj,
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            custom_encoder=custom_encoder,
            sqlalchemy_safe=sqlalchemy_safe,
        )
    if isinstance(obj, Enum):
        return obj.value
    if isinstance(obj, PurePath):
        return str(obj)
    if isinstance(obj, (str, int, float, type(None))):
        return obj
    if isinstance(obj, dict):
        return _encode_dict(
            obj,
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            custom_encoder=custom_encoder,
            sqlalchemy_safe=sqlalchemy_safe,
        )
    if isinstance(obj, (list, set, frozenset, GeneratorType, tuple)):
        return _encode_iterable(
            obj,
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            custom_encoder=custom_encoder,
            sqlalchemy_safe=sqlalchemy_safe,
        )
    if custom_encoder:
        return _encode_custom(
            obj,
            custom_encoder=custom_encoder,
            sqlalchemy_safe=sqlalchemy_safe,
        )
    return _encode_default(
        obj,
        sqlalchemy_safe=sqlalchemy_safe,
    )


def _encode_base_model(
    obj: BaseModel,
    include: Optional[Union[SetIntStr, DictIntStrAny]] = None,
    exclude: Optional[Union[SetIntStr, DictIntStrAny]] = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    custom_encoder: Dict[Any, Callable[[Any], Any]] = {},
    sqlalchemy_safe: bool = True,
) -> Any:
    encoder = getattr(obj.__config__, "json_encoders", {})
    if custom_encoder:
        encoder.update(custom_encoder)
    obj_dict = obj.dict(
        include=include,  # type: ignore # in Pydantic
        exclude=exclude,  # type: ignore # in Pydantic
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_none=exclude_none,
        exclude_defaults=exclude_defaults,
    )
    if "__root__" in obj_dict:
        obj_dict = obj_dict["__root__"]
    return jsonable_encoder(
        obj_dict,
        exclude_none=exclude_none,
        exclude_defaults=exclude_defaults,
        custom_encoder=encoder,
        sqlalchemy_safe=sqlalchemy_safe,
    )


def _encode_dict(
    obj: Dict[Any, Any],
    include: Optional[Union[SetIntStr, DictIntStrAny]] = None,
    exclude: Optional[Union[SetIntStr, DictIntStrAny]] = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    custom_encoder: Dict[Any, Callable[[Any], Any]] = {},
    sqlalchemy_safe: bool = True,
) -> Dict[Any, Any]:
    encoded_dict = {}
    for key, value in obj.items():
        if (
            (
                not sqlalchemy_safe
                or (not isinstance(key, str))
                or (not key.startswith("_sa"))
            )
            and (value is not None or not exclude_none)
            and ((include and key in include) or not exclude or key not in exclude)
        ):
            encoded_key = jsonable_encoder(
                key,
                by_alias=by_alias,
                exclude_unset=exclude_unset,
                exclude_none=exclude_none,
                custom_encoder=custom_encoder,
                sqlalchemy_safe=sqlalchemy_safe,
            )
            encoded_value = jsonable_encoder(
                value,
                by_alias=by_alias,
                exclude_unset=exclude_unset,
                exclude_none=exclude_none,
                custom_encoder=custom_encoder,
                sqlalchemy_safe=sqlalchemy_safe,
            )
            encoded_dict[encoded_key] = encoded_value
    return encoded_dict


def _encode_iterable(
    obj: Union[list, set, frozenset, GeneratorType, tuple],
    include: Optional[Union[SetIntStr, DictIntStrAny]] = None,
    exclude: Optional[Union[SetIntStr, DictIntStrAny]] = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    custom_encoder: Dict[Any, Callable[[Any], Any]] = {},
    sqlalchemy_safe: bool = True,
) -> List[Any]:
    encoded_list = []
    for item in obj:
        encoded_list.append(
            jsonable_encoder(
                item,
                include=include,
                exclude=exclude,
                by_alias=by_alias,
                exclude_unset=exclude_unset,
                exclude_defaults=exclude_defaults,
                exclude_none=exclude_none,
                custom_encoder=custom_encoder,
                sqlalchemy_safe=sqlalchemy_safe,
            )
        )
    return encoded_list


def _encode_custom(
    obj: Any,
    custom_encoder: Dict[Any, Callable[[Any], Any]],
    sqlalchemy_safe: bool = True,
) -> Any:
    if type(obj) in custom_encoder:
        return custom_encoder[type(obj)](obj)
    else:
        for encoder_type, encoder in custom_encoder.items():
            if isinstance(obj, encoder_type):
                return encoder(obj)


def _encode_default(
    obj: Any,
    sqlalchemy_safe: bool = True,
) -> Any:
    if type(obj) in ENCODERS_BY_TYPE:
        return ENCODERS_BY_TYPE[type(obj)](obj)
    for encoder, classes_tuple in encoders_by_class_tuples.items():
        if isinstance(obj, classes_tuple):
            return encoder(obj)
    errors: List[Exception] = []
    try:
        data = dict(obj)
    except Exception as e:
        errors.append(e)
        try:
            data = vars(obj)
        except Exception as e:
            errors.append(e)
            raise ValueError(errors)
    return jsonable_encoder(
        data,
        sqlalchemy_safe=sqlalchemy_safe,
    )
