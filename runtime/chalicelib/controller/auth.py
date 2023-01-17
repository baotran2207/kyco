import math
import random

from chalicelib.events.base import EventType, post_event
from chalicelib.logger_app import logger
from chalicelib.schemas import UserSignIn
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
    username,
    challenge_session_id,
    challenge_answer,
    authenticator: Authenticator = cog_authenticator,
):

    verified_user = authenticator.verify_challenge(
        username=username,
        challenge_session_id=challenge_session_id,
        challenge_answer=challenge_answer,
    )
    return verified_user


def send_email_otp():
    pass


def send_sms_otp():
    pass


def sign_up(user, authenticator: Authenticator = cog_authenticator):
    # post_event(EventType.PRE_USER_REGISTER, user)
    logger.info(user)
    created_user = authenticator.sign_up(user)
    # created_user = {"uuid": "test-sdsdsds"}

    # post_event(EventType.POST_USER_REGISTER, user)

    return created_user


def sign_up_with_otp():
    pass


def login_with_password():
    pass


def login_with_otp():
    pass


def generate_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP
