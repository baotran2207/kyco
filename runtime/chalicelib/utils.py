import json
import math
import random
import secrets
import string
from pprint import pprint

from chalicelib.logger_app import logger


def generate_new_password(password_length=8) -> str:
    return "".join(
        (
            secrets.choice(string.ascii_letters + string.digits + string.punctuation)
            for i in range(password_length)
        )
    )


def generate_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP


def to_snake_key(char: str) -> str:
    return char.replace(" ", "_").lower()


def parse_sqs_record_to_email_messages(record_dict: dict) -> dict:
    message_attributes = record_dict.get("messageAttributes", {})

    cc_emails = json.loads(message_attributes.get("cc_emails", {}).get("stringValue", "[]"))
    bcc_emails = json.loads(message_attributes.get("bcc_emails", {}).get("stringValue", "[]"))
    reply_tos = json.loads(message_attributes.get("reply_tos", {}).get("stringValue", "[]"))

    email_type = message_attributes.get("message_type", {}).get("stringValue", "")
    email_payload = json.loads(
        message_attributes.get("message_payload", {}).get("stringValue", "")
    )
    res = {
        # required
        "to_emails": json.loads(message_attributes.get("to_emails", {}).get("stringValue")),
        "source": message_attributes.get("source", {}).get("stringValue"),
        "email_type": email_type,
        "email_payload": email_payload,
        # non required
        "cc_emails": cc_emails,
        "bcc_emails": bcc_emails,
        "reply_tos": reply_tos,
    }

    return res
