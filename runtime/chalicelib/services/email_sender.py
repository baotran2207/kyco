import json
from dataclasses import dataclass
from typing import Optional, Protocol, Union

import boto3
from chalicelib.config import settings
from chalicelib.logger_app import logger
from chalicelib.schemas.emails import EmailMessage, EmailTemplatedMessage
from chalicelib.services.ses_service import ses_mail_sender
from chalicelib.services.sqs_service import send_email_queue
from pydantic import EmailStr

SES_FROM_ADDRESS = settings.WEBMASTER_EMAIL


# source, destination, subject, text, html, reply_tos=None)
def enqueue_send_email(
    to_emails: list[EmailStr],
    message_type: str,
    message_payload: dict = None,
    template_name: Optional[str] = None,
    cc_emails: list[EmailStr] = [],
    bcc_emails: list[EmailStr] = [],
    reply_tos: list[EmailStr] = [],
    source: EmailStr = SES_FROM_ADDRESS,
):
    if template_name:
        email_message = EmailTemplatedMessage(
            to_emails=to_emails,
            email_payload=message_payload,
            source=source,
            template_name=template_name,
            cc_emails=cc_emails,
            bcc_emails=bcc_emails,
            reply_tos=reply_tos,
        )
    else:
        email_message = EmailMessage(
            to_emails=to_emails,
            email_payload=message_payload,
            source=source,
            cc_emails=cc_emails,
            bcc_emails=bcc_emails,
            reply_tos=reply_tos,
        )

    logger.info(f"message_attributes : {email_message}")
    send_email_queue(
        message_body=f"sending email {message_type}",
        message_attributes=email_message.dict(),
    )
    logger.info(f"queued an email with message subject : {template_name}")


send_email = enqueue_send_email


def send_admin_email(subject: str, message: str):
    enqueue_send_email(
        to_emails=settings.ADMIN_EMAILS,
        message_type="ADMIN_EMAIL",
        message_payload={
            "message": message,
            "subject": subject,
        },
    )
