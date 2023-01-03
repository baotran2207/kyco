import logging

# from aws_lambda_powertools import Logger
from chalicelib.config import settings
from chalicelib.enums import AppEnv

if AppEnv.dev.value == settings.ENV:
    from rich.logging import RichHandler

logger = logging.getLogger(settings.PROJECT_NAME)


def init_logger(app):
    if AppEnv.prod.value == settings.ENV:
        app.log.setLevel(logging.INFO)
    else:
        app.log.setLevel(logging.DEBUG)
        app.log.handlers = [RichHandler()]
    logger = app.log

    logger.info(f"Logger is ready ! Level : {logger.level}")
    return app
