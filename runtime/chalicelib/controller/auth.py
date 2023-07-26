import math
import random

from chalicelib.events.base import EventType, post_event
from chalicelib.logger_app import logger
from chalicelib.schemas import (
    TokenPayload,
    UserAdminChangePassword,
    UserChangePassword,
    UserConfirmForgotPassword,
    UserSignIn,
)
from chalicelib.services.authorizers import Authenticator
from chalicelib.services.authorizers import authenticator as cog_authenticator


def login(user: UserSignIn, authenticator: Authenticator = cog_authenticator):
    response = authenticator.sign_in(user.username, user.password)
    return response


def lookup_user(user: UserSignIn, authenticator: Authenticator = cog_authenticator):
    response = authenticator.get_user(user.username)
    return response


def init_challenge(username, authenticator: Authenticator = cog_authenticator):
    return authenticator.init_challenge(username=username)


def login_with_challenge(
    username: str,
    challenge_session_id: str,
    challenge_answer: str,
    authenticator: Authenticator = cog_authenticator,
):
    return authenticator.verify_challenge(
        username=username,
        challenge_session_id=challenge_session_id,
        challenge_answer=challenge_answer,
    )


def sign_up(user, authenticator: Authenticator = cog_authenticator):
    # post_event(EventType.PRE_USER_REGISTER, user)
    logger.info(user)
    created_user = authenticator.sign_up(user)
    # post_event(EventType.POST_USER_REGISTER, user)

    return created_user


def get_users(authenticator: Authenticator = cog_authenticator):
    return authenticator.get_users()


def get_user(access_token: str, authenticator: Authenticator = cog_authenticator):
    return authenticator.get_user(access_token)


def initiate_forgot_password(
    username: str, authenticator: Authenticator = cog_authenticator
):
    return authenticator.initiate_forgot_password(username)


def confirm_forgot_password(
    user: UserConfirmForgotPassword, authenticator: Authenticator = cog_authenticator
):
    return authenticator.confirm_forgot_password(
        user.username,
        user.confirmation_code,
        user.new_password,
    )


def change_password(
    user: UserChangePassword, authenticator: Authenticator = cog_authenticator
):
    return authenticator.change_password(
        user.access_token,
        user.old_password,
        user.new_password,
    )
