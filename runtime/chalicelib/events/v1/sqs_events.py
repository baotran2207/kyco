from chalice import Blueprint
from chalice.app import SQSEvent
from chalicelib.config import settings
from chalicelib.logger_app import logger
from chalicelib.schemas.emails import EmailMessage, EmailTemplatedMessage
from chalicelib.services.ses_service import ses_mail_sender
from chalicelib.services.sqs_service import (
    delete_messages,
    get_queue,
    parse_sqs_message_attrs_to_dict,
)

sqs_bp = Blueprint(__name__)


def parse_sqs_record_to_email_messages(record_dict: dict) -> EmailMessage | EmailTemplatedMessage:
    message_attributes = parse_sqs_message_attrs_to_dict(record_dict["messageAttributes"])
    logger.info(message_attributes)
    template_name = message_attributes.get("template_name", "")
    if template_name:
        email_message = EmailTemplatedMessage(
            **message_attributes,
        )
    else:
        email_message = EmailMessage(**message_attributes)
    return email_message


def _handle_sqs_email(record_dict: dict):
    email_message = parse_sqs_record_to_email_messages(record_dict)
    logger.info(email_message.dict())
    if email_message.template_name:
        ses_mail_sender.send_templated_email(
            to_emails=email_message.to_emails,
            template_name=email_message.template_name,
            template_data=email_message.email_payload,
            source=email_message.source,
            cc_emails=email_message.cc_emails,
            bcc_emails=email_message.bcc_emails,
            reply_tos=email_message.reply_tos,
        )

    else:
        ses_mail_sender.send_email(
            to_emails=email_message.get("to_emails"),
            message=email_message.email_payload,
            source=email_message.get("source"),
            cc_emails=email_message.get("cc_emails"),
            bcc_emails=email_message.get("bcc_emails"),
            reply_tos=email_message.get("reply_tos"),
        )

    logger.debug(f"Sent email {email_message.dict()}")
    return True


@sqs_bp.on_sqs_message(queue_arn=settings.SQS_GENERIC, batch_size=10)
def handle_sqs_generic(event: SQSEvent):
    for record in event:
        body = record.body
        logger.debug(body)
        logger.info(f" in even ! Detail {record} ")


@sqs_bp.on_sqs_message(queue_arn=settings.SQS_SENDEMAIL, batch_size=10)
def handle_sqs_email(event: SQSEvent):
    success_msgs = []
    error_msgs = []

    for record in event:
        record_dict = record.to_dict()
        logger.info(record_dict)

        try:
            _handle_sqs_email(record_dict)
            success_msgs.append(record)
        except Exception as e:
            logger.error(f"Error when sending email {record.body} . Detail {e}")
            # dead letter queue
            error_msgs.append(record)
            logger.error(e)
            raise e
        finally:
            delete_messages(
                queue=get_queue(settings.SQS_SENDEMAIL),
                messages=success_msgs,
            )
