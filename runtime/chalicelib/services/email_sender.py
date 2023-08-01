import json
from dataclasses import dataclass
from typing import Protocol, Union

import boto3
from chalicelib.config import settings
from chalicelib.logger_app import logger
from chalicelib.services.email_render import (
    get_new_otp_message,
    render_porfolio_message,
)
from chalicelib.services.sqs_service import send_email_queue
from pydantic import EmailStr

SES_FROM_ADDRESS = settings.WEBMASTER_EMAIL


# source, destination, subject, text, html, reply_tos=None)
def enqueue_send_email(
    to_emails: Union[list, str],
    message_type: str,
    message_payload: dict = None,
    cc_emails: list[EmailStr] = None,
    bcc_emails: list[EmailStr] = None,
    reply_tos: list[EmailStr] = None,
    source: EmailStr = SES_FROM_ADDRESS,
):
    if isinstance(to_emails, str):
        to_emails = [to_emails]
    message_attributes = {
        "to_emails": json.dumps(to_emails),
        "message_type": message_type,
        "message_payload": json.dumps(message_payload),
        "source": source,
    }
    if cc_emails:
        message_attributes["cc_emails"] = json.dumps(cc_emails)
    if bcc_emails:
        message_attributes["bcc_emails"] = json.dumps(bcc_emails)

    send_email_queue(
        message_body=f"sending email {message_type}",
        message_attributes=message_attributes,
    )
    logger.info(f"enqueue email to {to_emails} with message subject : {message_type}")


# def send_porfolio_overview(emails, values):
#     message = render_porfolio_message(values)
#     return enqueue_send_email(emails, message)
