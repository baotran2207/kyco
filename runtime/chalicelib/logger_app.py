import logging

# from aws_lambda_powertools import Logger
from chalicelib.config import settings
from chalicelib.enums import AppEnv
from rich.logging import RichHandler

logging.basicConfig(
    level=logging.DEBUG if AppEnv.dev.value == settings.ENV else logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
)
logger = logging.getLogger(settings.PROJECT_NAME)

logger.info(f"Logger is ready ! Level : {logger.level} !")

# if AppEnv.dev.value == settings.ENV:

logger.addHandler(RichHandler())
logger.debug("Added RichHandler for debug purpose")

logger.error("Dummy Error")
logger.debug("Dummy Debug")
logger.warning("Warning")

logger.info(logger.level)
