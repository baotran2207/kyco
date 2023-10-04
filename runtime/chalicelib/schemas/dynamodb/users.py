from typing import Optional, Protocol

from pydantic import BaseModel, validator


class CustomBaseModel(BaseModel):
    def toJSON(self):
        return self.dict()

    def dict(self):
        return self.__dict__


class Item(CustomBaseModel):
    hash_key: str
    sort_key: str
    attributes: dict


class User(Item):
    """USER#user_sub"""

    @validator
    def validate_hash_key(cls, v):
        if not v.startwiths("USER#"):
            raise ValueError("hash_key must start with USER#")
        return v


class Portfolio(Item):
    """PORTFOLIO#user_sub#porf_name"""

    @validator
    def validate_hash_key(cls, v):
        if not v.startwiths("PORTFOLIO#"):
            raise ValueError("hash_key must be PORTFOLIO#")
        return v


class Deposit(Item):
    """DEPOSIT#user_sub#KSUD_DEPOSITID"""

    @validator
    def validate_hash_key(cls, v):
        if not v.startwiths("Deposit#"):
            raise ValueError("hash_key must be Deposit#")
        return v


class ORDER(Item):
    """DEPOSIT#user_sub#KSUD_DEPOSITID"""

    @validator
    def validate_hash_key(cls, v):
        if not v.startwiths("Deposit#"):
            raise ValueError("hash_key must be Deposit#")
        return v
