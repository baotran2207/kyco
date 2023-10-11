"""
    Coginto events need to be configurea via console once
"""
import json

from chalice import Blueprint
from chalicelib.config import settings
from chalicelib.enums import EmailType
from chalicelib.logger_app import logger
from chalicelib.services.email_render import get_email_template
from chalicelib.services.email_sender import send_email
from chalicelib.utils import generate_otp

cognito_post_config_bp = Blueprint(__name__)


# sign up
@cognito_post_config_bp.lambda_function()
def pre_sign_up(event, context):
    logger.info("Pre sing up")


# sign in


@cognito_post_config_bp.lambda_function()
def pre_authentication(event, context):
    logger.info("pre_authentication")
    return event


@cognito_post_config_bp.lambda_function()
def post_authentication(event, context):
    logger.info("post_authentication")
    custom_response = {"message": "custom post_authentication"}
    return event | {"response": custom_response}


@cognito_post_config_bp.lambda_function()
def post_confirmation(event, context):
    logger.info("post_confirmation")
    return event


# custom message
@cognito_post_config_bp.lambda_function()
def pre_custom_message(event, context):
    logger.info("pre_custom_message")
    custom_response = {
        "smsMessage": "Hello from tranthanhbao",
        "emailMessage": "Hello from tranthanhbao",
        # "emailSubject": "string"
    }
    return event | {"response": custom_response}


# CUSTOM auth challenge
# https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-define-auth-challenge.html#aws-lambda-triggers-define-auth-challenge-example
@cognito_post_config_bp.lambda_function()
def create_auth_challenge(event, context):
    logger.info("create_auth_challenge")
    # return event
    otp = str(generate_otp())
    custom_response = {
        "publicChallengeParameters": {
            "publicChallenge": "something",
        },
        "privateChallengeParameters": {
            "challengeAnswer": otp,
        },
        "challengeMetadata": "event with otp",
    }
    # send_notify
    email = event["request"]["userAttributes"].get("email")
    logger.info(f"template name {get_email_template(EmailType.NEW_OTP.value)}")
    if email:
        send_email(
            to_emails=[email],
            message_type=EmailType.NEW_OTP.value,
            message_payload={
                "otp_code": otp,
                "template_name": get_email_template(EmailType.NEW_OTP.value),
            },
        )

    res = event | {"response": custom_response}

    return res


@cognito_post_config_bp.lambda_function()
def define_auth_challenge(event, context):
    logger.info("define_auth_challenge")
    user_not_found = event["request"]["userNotFound"]
    if user_not_found:
        return event | {
            "failAuthentication": True,
            "issueTokens": False,
        }

    session = event["request"]["session"]
    if len(session) > 0 and session[-1]["challengeResult"]:
        logger.info("Verified challenge")
        custom_response = {
            "issueTokens": True,
            "failAuthentication": False,
        }
        return event | {"response": custom_response}

    custom_response = {
        "challengeName": "CUSTOM_CHALLENGE",
        "issueTokens": False,
        "failAuthentication": False,
    }
    return event | {"response": custom_response}


@cognito_post_config_bp.lambda_function()
def verify_auth_challenge(event, context):
    expected_answer = event["request"]["privateChallengeParameters"]["challengeAnswer"]
    user_answer = event["request"]["challengeAnswer"]
    return event | {
        "response": {"answerCorrect": str(expected_answer) == str(user_answer)}
    }
