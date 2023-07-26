from typing import Union

import boto3
from chalicelib.config import settings
from chalicelib.logger_app import logger
from chalicelib.services.email_render import (
    get_new_otp_message,
    render_porfolio_message,
)
from chalicelib.services.sqs_service import send_email_queue

ses = boto3.client("ses")

SES_FROM_ADDRESS = settings.WEBMASTER_EMAIL


# source, destination, subject, text, html, reply_tos=None)
def send_email(
    to_emails: Union[list, str],
    message: str,
    cc_emails: list = None,
    bcc_emails: list = None,
    reply_tos: list = None,
    source: str = SES_FROM_ADDRESS,
):
    if isinstance(to_emails, str):
        to_emails = [to_emails]

    send_email_queue(
        message_body="sending email",
        message_attributes={
            "to_emails": to_emails,
            "cc_emails": cc_emails,
            "bcc_emails": bcc_emails,
            "email_message": message,
            "reply_tos": reply_tos,
            "source": source,
        },
    )
    logger.info(
        f"enqueue email to {to_emails} with message subject : {message.get('Subject')}"
    )


def send_otp(email, otp_value):
    message = get_new_otp_message(otp_value)
    return send_email(email, message)


def send_porfolio_overview(emails, values):
    message = render_porfolio_message(values)
    return send_email(emails, message)
