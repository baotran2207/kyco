import logging

from aws_lambda_powertools import Logger
from chalicelib.config import settings

logger = logging.getLogger(settings.PROJECT_NAME)
logger.setLevel(logging.INFO)
