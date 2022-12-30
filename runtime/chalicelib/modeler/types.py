## custom type

# -*- encoding: utf-8 -*-
"""Definitions of datatypes and enums and such

Note for the future: presently Datamaster Enums are fairly arbitrary
and can mean anything. There is a number of exceptions which actually
do (in part) correspond to some specific behaviour but in many other
cases, the data only exists for display purposes.

It would generally be preferable to use something like PostgreSQL
Enums here instead, but there we again return to the problem of not
dealing with "semantic" labels (those that do something) and
"non-semantic" labels or values (changing the values doesn't change
anything in how Datamaster operates).

To make matters somewhat worse, the numeric IDs can differ for certain
Enums and different customers can have completely different values for
them.
"""

import codecs
import csv
import datetime as dt
import os
import re
import sys
from builtins import *
from collections import OrderedDict
from itertools import chain

import sqlalchemy.types as types
from flask_babelex import gettext as _gettext

# SQLAlchemy does not map BigInt to Int by default on the sqlite dialect.
from sqlalchemy.dialects import mysql, postgresql, sqlite

BigInt = types.BigInteger()
BigInt = BigInt.with_variant(postgresql.BIGINT(), "postgresql")
BigInt = BigInt.with_variant(mysql.BIGINT(), "mysql")
BigInt = BigInt.with_variant(sqlite.INTEGER(), "sqlite")


class CharBool(types.UserDefinedType):
    def python_type(self):
        return bool

    def get_col_spec(self):
        return "CHAR(1) NOT NULL DEFAULT 'F'"

    def bind_processor(self, dialect):
        def process(value):
            # Hacky but this is a quick workaround for SQLAlchemy
            # serializing False as "false" (without quotes).
            return "T" if value in (True, "T") else "F"

        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            return value == "T"

        return process


class FailEnum(types.UserDefinedType):
    """Simple validation for numeric enum types.

    The name 'FailEnum' is since this is an improper implementation
    without even any CHECK constraints.

    This does, however, attempt some form of validation of input
    values. Only explicitly mapped integers are allowed.

    An unmapped zero is allowed for backwards compatibility and
    translates to NULL.

    The code is a bit of a mess because this class used to do
    integer<->string mapping.
    """

    def __init__(self, *enums, **kw):
        super(FailEnum, self).__init__()
        self.name = kw.get("name")
        if "localizations" in kw:
            self.localizations = kw["localizations"]
        if "dict_" in kw:
            self.enums = kw["dict_"]
        else:
            mapping = (
                kw["mapping"] if "mapping" in kw else list(range(1, len(enums) + 1))
            )
            self.enums = dict(list(zip(mapping, enums)))

        # Ensure we always display enum values in ascending id order.
        self.enums = OrderedDict((k, v) for k, v in sorted(self.enums.items()))

        # Set enum symbolic aliases:
        for num, name in self.enums.items():
            setattr(self, name, num)

    def get_col_spec(self):
        # Actually BIGINT is used but that's way too excessive.
        return "SMALLINT"

    def bind_processor(self, dialect):
        def process(value):
            try:
                if value:
                    value = int(value)
            except Exception as e:
                print(
                    "ERROR: failed to process enum value {}. Not an integer!".format(
                        value
                    )
                )
                return None
            if value == 0 and 0 not in self.enums:
                return None
            elif value is not None and value not in self.enums:
                print(
                    "Invalid value for Enum {}: {} ({})".format(
                        self.name, repr(value), self.enums
                    ),
                    file=sys.stderr,
                )
            return value

        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            try:
                if value:
                    value = int(value)
            except Exception as e:
                print(
                    "ERROR: failed to process enum value {}. Not an integer!".format(
                        value
                    )
                )
                return None
            if value == 0 and 0 not in self.enums:
                return None
            elif value is not None and value not in self.enums:
                print(
                    "Invalid value for Enum {}: {}".format(self.name, value),
                    file=sys.stderr,
                )
            return value

        return process

    def adapt(self, cls, **kw):
        """This seems to be the easiest way to make this work.

        Without this, the impl class would be re-initialized 'empty'.
        """
        enums = list(self.enums.items())
        return cls(
            *(name for id, name in enums),
            mapping=(id for id, name in enums),
            **dict((k, v) for k, v in chain([("name", self.name)], iter(kw.items())))
        )


class TextEnum(FailEnum):
    def get_col_spec(self):
        # Actually BIGINT is used but that's way too excessive.
        return "varchar(20)"


Enum = FailEnum
