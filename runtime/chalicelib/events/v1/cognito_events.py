"""
    Coginto events need to be configurea via console once

"""
from chalice import Blueprint
from chalicelib.config import settings
from chalicelib.logger_app import logger

cognito_post_config_bp = Blueprint(__name__)

"""
TODO: not in used yet ! still under configuired

"""

@cognito_post_config_bp.lambda_function()
def pre_sign_up(event, context):
    logger.info("Pre sing up")
    print(event)


@cognito_post_config_bp.lambda_function()
def pre_authentication(event, context):
    logger.info("pre_authentication")
    print(event)


@cognito_post_config_bp.lambda_function()
def post_authentication(event, context):
    logger.info("post_authentication")
    print(event)


@cognito_post_config_bp.lambda_function()
def post_confirmation(event, context):
    logger.info("post_confirmation")
    print(event)


@cognito_post_config_bp.lambda_function()
def pre_custom_message(event, context):
    logger.info("pre_custom_message")
    print(event)


@cognito_post_config_bp.lambda_function()
def create_auth_challenge(event, context):
    logger.info("create_auth_challenge")
    print(event)
