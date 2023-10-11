import json
from dataclasses import dataclass

import boto3
from botocore.exceptions import ClientError, WaiterError
from chalicelib.config import settings
from chalicelib.logger_app import logger
from pydantic import EmailStr


@dataclass
class SesMailSender:
    def __init__(self, ses_client):
        self.ses_client = ses_client

    def send_email(
        self,
        to_emails: list[EmailStr],
        message: dict,
        source: EmailStr,
        cc_emails: list[EmailStr] | None = [],
        bcc_emails: list[EmailStr] | None = [],
        reply_tos: list[EmailStr] | None = [],
    ) -> str:
        """
        :return: The ID of the message, assigned by Amazon SES.
        """
        send_args = {
            "Source": source,
            "Destination": {
                "ToAddresses": to_emails,
                "CcAddresses": cc_emails,
                "BccAddresses": bcc_emails,
            },
            "Message": message,
            "ReplyToAddresses": reply_tos,
        }
        try:
            response = self.ses_client.send_email(**send_args)
            message_id = response["MessageId"]
            logger.info("Sent mail %s from %s to %s.", message_id, source, to_emails)
        except ClientError:
            logger.exception("Couldn't send mail from %s to %s.", source, to_emails)
            raise
        else:
            return message_id

    def send_templated_email(
        self,
        to_emails: list[EmailStr],
        template_name: str,
        template_data: dict | str,
        source: EmailStr,
        cc_emails: list[EmailStr] | None = None,
        bcc_emails: list[EmailStr] | None = None,
        reply_tos: list[EmailStr] | None = None,
    ) -> str:
        """
        Sends an email based on a template. A template contains replaceable tags
        each enclosed in two curly braces, such as {{name}}. The template data passed
        in this function contains key-value pairs that define the values to insert
        in place of the template tags.

        Note: If your account is in the Amazon SES  sandbox, the source and
        destination email accounts must both be verified.

        :return: The ID of the message, assigned by Amazon SES.
        """
        template_payload = (
            json.dumps(template_data)
            if isinstance(template_data, dict)
            else template_data
        )

        send_args = {
            "Source": source,
            "Destination": {
                "ToAddresses": to_emails,
                "CcAddresses": cc_emails,
                "BccAddresses": bcc_emails,
            },
            "Template": template_name,
            "TemplateData": template_payload,
        }
        if reply_tos is not None:
            send_args["ReplyToAddresses"] = reply_tos
        try:
            response = self.ses_client.send_templated_email(**send_args)
            message_id = response["MessageId"]
            logger.info(
                "Sent templated mail %s from %s to %s.",
                message_id,
                source,
                to_emails,
            )
        except ClientError:
            logger.exception(
                "Couldn't send templated mail from %s to %s.", source, to_emails
            )
            raise
        else:
            return message_id


ses_client = boto3.client("ses")
ses_mail_sender = SesMailSender(ses_client)
