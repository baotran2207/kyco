from dataclasses import dataclass
from typing import Protocol

from botocore.exceptions import ClientError
from chalicelib.events.base import EventType, post_event
from chalicelib.logger_app import logger
from chalicelib.schemas import UserCreate, UserSignIn
from chalicelib.services.authorizers import Authenticator
from chalicelib.services.authorizers import authenticator as current_authenticator

# def login_user(user: UserSignIn, authenticator: Authenticator = current_authenticator):
#     response = authenticator.sign_in(user)
#     return response


# def login_user_with_password(
#     user: UserSignIn, authenticator: Authenticator = current_authenticator
# ):
#     response = authenticator.sign_in(user)
#     return response


# def login_user_with_passwordless(
#     user: UserSignIn, authenticator: Authenticator = current_authenticator
# ):
#     response = authenticator.sign_in(user)
#     return response


# def password_forgotten(
#     user: UserSignIn, authenticator: Authenticator = current_authenticator
# ):
#     pass


# def reset_password(
#     user: UserSignIn, authenticator: Authenticator = current_authenticator
# ):
#     pass
