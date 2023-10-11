import json

from chalicelib.config import settings
from chalicelib.enums import EmailType
from chalicelib.events.v1.sqs_events import (
    _handle_sqs_email,
    parse_sqs_record_to_email_messages,
)
from chalicelib.services.email_render import get_email_template

email_message_fixture = {
    "messageId": "357ef346-f369-47e6-a67a-656148e297ff",
    "receiptHandle": "AQEBapZ6yWax1xBMUGRHMnoNUqYUd6o3T5HYsAyfK3ivzcg2VxeNPTJApY1GHDkioqWK1+Xvndz4T44UQwnUJJcETWKXQft43IvgSLZA/grATdaPOkKRmw1yKFkyxLiuZzah1mtXTNYp9iuUfhOR4PTweZRd5bjPednaGc7D1Ry+B7STjp2h2eNt8bZbhr5VsBKNaWZlpFLfq5DDnP5hZRaAFTS638j9JkAMJs+3EVvj5eMmWrPSC1ezoshU6CpJwnkrKv9/P0HlQ1d528VWoby6ekZOTn3Q6vRqvxRamVF9PlNCUGxp56KahFF0G93ahdjcck96sjvXWiXhG4hvfOmtS/uDpORn6l//nli/PWY4cAqS77eVO2Rv9lvxzncNk8w2HleCFIFLFxnmcCMOFF2lLQ==",
    "body": "sending email NEW_OTP",
    "attributes": {
        "ApproximateReceiveCount": "2",
        "AWSTraceHeader": "Root=1-65263746-320c824c58b9e15b51a84f99;Parent=7dcee31f3d8a37a0;Sampled=0;Lineage=b92f77be:0",
        "SentTimestamp": "1697003336218",
        "SenderId": "AROA2UDD5TARNC7GJDOXE:kyco-chalice-id-CreateAuthChallenge-LEyiQTWMzQ01",
        "ApproximateFirstReceiveTimestamp": "1697003336219",
    },
    "messageAttributes": {
        "to_emails": {
            "stringValue": '["tranthanhbao2207@gmail.com"]',
            "stringListValues": [],
            "binaryListValues": [],
            "dataType": "String",
        },
        "message_payload": {
            "stringValue": '{"otp_code": "1607", "template_name": "KycoNEW_OTP"}',
            "stringListValues": [],
            "binaryListValues": [],
            "dataType": "String",
        },
        "message_type": {
            "stringValue": "NEW_OTP",
            "stringListValues": [],
            "binaryListValues": [],
            "dataType": "String",
        },
        "source": {
            "stringValue": "tranthanhbao2207@gmail.com",
            "stringListValues": [],
            "binaryListValues": [],
            "dataType": "String",
        },
    },
    "md5OfMessageAttributes": "86c507d9d4caf5d6cd91256791ff2985",
    "md5OfBody": "7b731c18c5298e39d947e563074a0aba",
    "eventSource": "aws:sqs",
    "eventSourceARN": "arn:aws:sqs:ap-southeast-1:730353997858:KycoSendemail",
    "awsRegion": "ap-southeast-1",
}


def test_parse_sqs_record_to_email_messages():
    res = parse_sqs_record_to_email_messages(email_message_fixture)
    # res = parse_sqs_record_to_email_messages(sqs_record)
    assert res is True


def test_get_email_template():
    PROJECT_NAME = settings.PROJECT_NAME

    assert (
        get_email_template(EmailType.NEW_OTP.value)
        == f"{PROJECT_NAME.capitalize()}{EmailType.NEW_OTP.value}"
    )


def test_handle_sqs_email():
    res = _handle_sqs_email(email_message_fixture)

    assert res == True
