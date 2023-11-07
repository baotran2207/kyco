import logging
import sys

# from aws_lambda_powertools import Logger
from chalicelib.config import settings
from chalicelib.enums import AppEnv

if settings.ENV in [AppEnv.dev.value, AppEnv.test.value]:
    from rich.logging import RichHandler

from loguru import logger

# logger = logging.getLogger(settings.PROJECT_NAME)
# logger.propagate = False
# logging_level = settings.LOGGING_LEVEL


# class ProdHandler(logging.StreamHandler):
#     def emit(self, record):
#         # record.levelname = record.levelname[:4]
#         super().emit(record)
#         if record.levelname == "ERROR":
#             print("send email Error")


# if settings.ENV in [AppEnv.dev.value, AppEnv.test.value]:

#     class DevHandler(RichHandler):
#         def emit(self, record):
#             # record.levelname = record.levelname[:4]
#             super().emit(record)
#             # if record.levelname == "ERROR":
#             #     print("Not send email Error")

#     logger.handlers = [
#         DevHandler(
#             level=logging_level,
#             show_time=False,
#             rich_tracebacks=True,
#         )
#     ]
# else:
#     FORMAT_STRING = "%(levelname)-8s [%(filename)s:%(lineno)d] %(message)s"
#     handler = ProdHandler(sys.stdout)
#     formatter = logging.Formatter(FORMAT_STRING)
#     handler.setFormatter(formatter)
#     handler.setLevel(logging_level)
#     logger.handlers = [handler]

# logger.setLevel(logging_level)
logger.info(f"Logger is ready ! Level : {settings.LOGGING_LEVEL}")
