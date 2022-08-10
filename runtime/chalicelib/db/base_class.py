import uuid as uuid_pkg
from email.policy import default
from typing import Any

from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from sqlalchemy.ext.declarative import as_declarative, declared_attr


# class MinBase:
#     pass
@as_declarative()
class Base:
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
