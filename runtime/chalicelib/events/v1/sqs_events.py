from chalice import Blueprint
from chalicelib.config import settings
from chalicelib.logger_app import logger

sqs_bp = Blueprint(__name__)


@sqs_bp.on_sqs_message(queue_arn=settings.SQS_GENERIC, batch_size=1)
def handle_sqs_generic(event):
    logger.info("Trigger generic")
    logger.info("dict ", event.to_dict())
    logger.info("body ", event.body)
    logger.info("body ", event.body)
    for record in event:
        logger.info(f" in even ! Detail {record} ")


@sqs_bp.on_sqs_message(queue_arn=settings.SQS_SENDEMAIL, batch_size=1)
def handle_sqs_email(event):
    logger.info("Trigger email")
    logger.info("dict ", event.to_dict())
    logger.info("body ", event.body)
    logger.info("body ", event.body)
    for record in event:
        logger.info(f" in even ! Detail {record} ")


