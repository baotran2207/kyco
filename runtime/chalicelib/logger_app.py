import logging
import sys
# from aws_lambda_powertools import Logger
from chalicelib.config import settings
from chalicelib.enums import AppEnv

if AppEnv.dev.value == settings.ENV:
    from rich.logging import RichHandler


logger = logging.getLogger(settings.PROJECT_NAME)
logger.propagate = False
logging_level = settings.LOGGING_LEVEL


if settings.ENV == AppEnv.dev.value:
    logger.handlers = [RichHandler(
        level=logging_level,
        show_time=False,
        rich_tracebacks=True,
    )]
else:
    FORMAT_STRING = "%(levelname)-8s [%(filename)s:%(lineno)d] %(message)s"
    handler = logging.StreamHandler(sys.stdout)
    formatter= logging.Formatter(FORMAT_STRING)
    handler.setFormatter(formatter)
    handler.setLevel(logging_level)
    logger.handlers = [handler]

logger.setLevel(logging_level)
logger.info(f"Logger is ready ! Level : {logging_level}")