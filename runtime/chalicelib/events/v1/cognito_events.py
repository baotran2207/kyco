"""
    Coginto events need to be configurea via console once

"""
from chalicelib.logger_app import logger


@app.lambda_function()
def pre_sign_up(event, context):
    logger.info("Pre sing up")
    print(event)


@app.lambda_function()
def pre_authentication(event, context):
    logger.info("pre_authentication")
    print(event)


@app.lambda_function()
def post_authentication(event, context):
    logger.info("post_authentication")
    print(event)


@app.lambda_function()
def post_confirmation(event, context):
    logger.info("post_confirmation")
    print(event)


@app.lambda_function()
def post_confirmation(event, context):
    logger.info("post_confirmation")
    print(event)


@app.lambda_function()
def create_auth_challenge(event, context):
    logger.info("create_auth_challenge")
    print(event)
