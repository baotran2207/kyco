"""
    Coginto events need to be configurea via console once

"""
import json

from chalice import Blueprint
from chalicelib.config import settings
from chalicelib.logger_app import logger
from chalicelib.services.email_sender import send_otp
from chalicelib.utils import generate_otp

cognito_post_config_bp = Blueprint(__name__)

"""
expample_event = {
    "version": "1",
    "region": "ap-southeast-1",
    "userPoolId": "ap-southeast-1_V5au3CS4P",
    "userName": "1f48aaf4-fc09-4478-9347-10500f3ddc2b",
    "callerContext": {
        "awsSdkVersion": "aws-sdk-unknown-unknown",
        "clientId": "l0ml6iavvgat4jbh3v84gprig",
    },
    "triggerSource": "PostAuthentication_Authentication",
    "request": {
        "userAttributes": {
            "sub": "1f48aaf4-fc09-4478-9347-10500f3ddc2b",
            "cognito:email_alias": "tranthanhbao2207@gmail.com",
            "cognito:user_status": "CONFIRMED",
            "email_verified": "true",
            "email": "tranthanhbao2207@gmail.com",
        },
        "newDeviceUsed": False,
    },
    "response": {},
}
"""


# sign up
@cognito_post_config_bp.lambda_function()
def pre_sign_up(event, context):
    logger.info("Pre sing up")
    print(event)


# sign in


@cognito_post_config_bp.lambda_function()
def pre_authentication(event, context):
    logger.info("pre_authentication")
    print(event)
    return event


@cognito_post_config_bp.lambda_function()
def post_authentication(event, context):
    logger.info("post_authentication")
    print(type(event), event)

    custom_response = {"message": "custom post_authentication"}
    return event | {"response": custom_response}


@cognito_post_config_bp.lambda_function()
def post_confirmation(event, context):
    logger.info("post_confirmation")
    print(event)
    return event


# custom message
@cognito_post_config_bp.lambda_function()
def pre_custom_message(event, context):
    logger.info("pre_custom_message")
    print(event)
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
    if email:
        send_otp(email=email, otp_value=otp)

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
