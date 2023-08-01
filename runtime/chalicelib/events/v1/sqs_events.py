from chalice import Blueprint
from chalice.app import SQSEvent, SQSRecord
from chalicelib.config import settings
from chalicelib.logger_app import logger
from chalicelib.services.email_render import EMAIL_RENDERS
from chalicelib.services.ses_service import ses_mail_sender
from chalicelib.services.sqs_service import delete_messages, get_queue
from chalicelib.utils import parse_sqs_record_to_email_messages
from typing_extensions import Protocol

sqs_bp = Blueprint(__name__)


@sqs_bp.on_sqs_message(queue_arn=settings.SQS_GENERIC, batch_size=10)
def handle_sqs_generic(event: SQSEvent):
    for record in event:
        body = record.body
        logger.debug(body)
        logger.info(f" in even ! Detail {record} ")


@sqs_bp.on_sqs_message(queue_arn=settings.SQS_SENDEMAIL, batch_size=10)
def handle_sqs_email(event: SQSEvent):
    success_msgs = []
    for record in event:
        record_dict = record.to_dict()
        logger.info(record_dict)
        msg_id = record_dict["messageId"]
        receipt_handle = record_dict["receiptHandle"]
        logger.info(f" in even ! Detail {msg_id} - {receipt_handle} ")

        email_message = parse_sqs_record_to_email_messages(record_dict)
        email_type = email_message.get("email_type")
        email_payload = email_message.get("email_payload")

        rendered_message = EMAIL_RENDERS.get(email_type)(email_payload)
        try:
            ses_mail_sender.send_email(
                to_emails=email_message.get("to_emails"),
                message=rendered_message,
                source=email_message.get("source"),
                cc_emails=email_message.get("cc_emails"),
                bcc_emails=email_message.get("bcc_emails"),
                reply_tos=email_message.get("reply_tos"),
            )
            success_msgs.append(record)
        except Exception as e:
            logger.error(f"Error when sending email {record.body} . Detail {e}")
            # dead letter queue
            raise e

    delete_messages(
        queue=get_queue(settings.SQS_SENDEMAIL),
        messages=success_msgs,
    )
