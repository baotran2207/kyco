from typing import Optional

from chalicelib.enums import *
from pydantic import BaseModel, EmailStr, fields, validator


class CustomBaseModel(BaseModel):
    def toJSON(self):
        return self.dict()


class UserBase(CustomBaseModel):
    uuid: str
    meta_data: dict


class UserCreate(CustomBaseModel):
    email: EmailStr
    password: str

    @validator("password")
    def is_long_enough(cls, value):
        if len(value) < 3:
            raise ValueError("password does not meet the requirements")
        return value


class UserUpdate(CustomBaseModel):
    password: Optional[str] = None


class User(CustomBaseModel):
    pass


class Token(CustomBaseModel):
    access_token: str
    token_type: str


class TokenPayload(CustomBaseModel):
    sub: Optional[list]


class UserSignIn(CustomBaseModel):
    email: EmailStr
    password: str


class UserLoginResponse(CustomBaseModel):
    # https://stackoverflow.com/questions/48543948/aws-cognito-whats-the-difference-between-access-and-identity-tokens
    AccessToken: str  # for external services , like aws ...
    ExpiresIn: int
    IdToken: str  # this is token for identity , our application chalice will use this as Authorization: Bearer <token>
    RefreshToken: str
    TokenType: str
