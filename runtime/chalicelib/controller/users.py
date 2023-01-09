from dataclasses import dataclass
from typing import Protocol

from botocore.exceptions import ClientError
from chalicelib.events.base import EventType, post_event
from chalicelib.logger_app import logger
from chalicelib.schemas import UserCreate, UserSignIn
from chalicelib.services.authorizers import Authenticator
from chalicelib.services.authorizers import authenticator as current_authenticator


def create_user(user: UserCreate, authenticator: Authenticator = current_authenticator):
    post_event(EventType.PRE_USER_REGISTER, user)
    logger.info(user)
    # created_user = authenticator.sign_up(user)
    created_user = {"uuid": "test-sdsdsds"}

    post_event(EventType.POST_USER_REGISTER, user)

    return created_user


def get_user(access_token: str, authenticator: Authenticator = current_authenticator):
    return authenticator.get_user(access_token)


def lookup_user(user):
    pass


def login_user(user: UserSignIn, authenticator: Authenticator = current_authenticator):
    response = authenticator.sign_in(user)
    return response


def password_forgotten(
    user: UserSignIn, authenticator: Authenticator = current_authenticator
):
    pass


def reset_password(
    user: UserSignIn, authenticator: Authenticator = current_authenticator
):
    pass
