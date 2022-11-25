from chalicelib.schemas import UserCreate, UserSignIn
from chalicelib.services.authorizers import Authenticator, authenticator as cog_authenticator
from typing import Protocol

from dataclasses import dataclass

from botocore.exceptions import ClientError

def create_user(user: UserCreate , authenticator: Authenticator=cog_authenticator):
    created_user = authenticator.sign_up(user)
    return created_user

def get_user(access_token: str, authenticator: Authenticator=cog_authenticator):
    return authenticator.get_user(access_token)

def login_user(user: UserSignIn, authenticator: Authenticator=cog_authenticator):
    response = authenticator.sign_in(user)
    return response


