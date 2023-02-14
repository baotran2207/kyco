import datetime as dt
import re
from typing import Optional

from chalicelib.enums import *
from pydantic import BaseModel, EmailStr, fields, validator


class CustomBaseModel(BaseModel):
    def toJSON(self):
        return self.dict()


class UserBase(CustomBaseModel):
    uuid: str
    meta_data: dict


class UserAuth(CustomBaseModel):
    email: Optional[EmailStr]
    phone_number: Optional[str]
    username: Optional[str]

    @validator("phone_number")
    def phone_validation(cls, v):
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if v and not re.search(regex, v, re.I):
            raise ValueError("Phone Number Invalid.")
        return v

    @validator("username", pre=True, always=True)
    def set_username(cls, v, *, values, **kwargs):
        phone_number = values.get("phone_number")
        email = values.get("email")

        username = v or email or phone_number
        if not username:
            raise ValueError("phone_number or email invalid !")

        if phone_number and email:
            logger.info(
                "Both phone_number and email are valid ! Email is set for username"
            )
        return username


class UserSignIn(UserAuth):
    password: Optional[str]


class UserSignInChallenge(UserAuth):
    challenge_session_id: str
    challenge_answer: str


class UserCreate(UserAuth):
    password: Optional[str]
    user_info: Optional[dict]


class UserUpdate(CustomBaseModel):
    password: Optional[str] = None


class User(CustomBaseModel):
    id: str
    created_at: dt.datetime
    lastchanged_at: dt.datetime
    cognito_id: Optional[str]
    email: Optional[EmailStr]
    phone_number: Optional[str]
    username: Optional[str]
    full_name: Optional[str]
    status: int
    is_superuser: bool = False

    @validator("username", pre=True, always=True)
    def set_username(cls, v, *, values, **kwargs):
        username = v or values.get("phone") or values.get("email")
        if not username:
            raise ValueError("Phone or email invalid !")
        return username


class Token(CustomBaseModel):
    access_token: str
    token_type: str


class TokenPayload(CustomBaseModel):
    sub: Optional[list]


class CognitoTokenPayload(CustomBaseModel):
    # https://stackoverflow.com/questions/48543948/aws-cognito-whats-the-difference-between-access-and-identity-tokens
    AccessToken: str  # for external services , like aws ...
    ExpiresIn: int
    IdToken: str  # this is token for identity , our application chalice will use this as Authorization: Bearer <token>
    RefreshToken: str
    TokenType: str


class UserLoginResponse(CognitoTokenPayload):
    pass
