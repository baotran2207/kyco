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


email_template_fixture = {
    "messageId": "d186d6f6-4ef5-4302-85c4-691f109c2fcf",
    "receiptHandle": "AQEBshav5iK+RF37lWXWTB9R0F4pwcOZsoQ1eCAtxt2leMQWW/tgZoW5AXRLUDQXSGl6PO2Pm2nprOaZNMJ7py9/ezfQJTKStwZPTMhkjd1cXt7FKk/LaEDhx5cUF6/r6jq/35a9YHtToglkzw2FFpnUb6QCqR5znSk+XB44pL5gJE3OLOJAjwSNPPoBX9732N6/EUenh+UxB0qAYIrawuMrZI0wPk79XQwv6jKBkCwDObukj9IRcZBj0VLflOqCHaLuUV8dHX37eoTCx4rNQFmfMdRQzVIzOCb3ixUQpXclgbTrqjFuTY1oOFd8on6sqLxaAGcs0IExyivh/4fqn1DOo/QIQl1UDZQ7yLUx/KcCEun7THXKvGXjGUfi96NKMKB426IUPtEyPC+w7EiwoK72zA==",
    "body": "sending email PORFOLIO_OVERVIEW",
    "attributes": {
        "ApproximateReceiveCount": "100",
        "SentTimestamp": "1699327751679",
        "SenderId": "AIDA2UDD5TARB5LUFFX5K",
        "ApproximateFirstReceiveTimestamp": "1699327751679",
    },
    "messageAttributes": {
        "to_emails": {
            "stringValue": "['tranthanhbao2207@gmail.com']",
            "stringListValues": [],
            "binaryListValues": [],
            "dataType": "String",
        },
        "template_name": {
            "stringValue": "Kyco_PORFOLIO_OVERVIEW",
            "stringListValues": [],
            "binaryListValues": [],
            "dataType": "String",
        },
        "cc_emails": {
            "stringValue": "[]",
            "stringListValues": [],
            "binaryListValues": [],
            "dataType": "String",
        },
        "reply_tos": {
            "stringValue": "[]",
            "stringListValues": [],
            "binaryListValues": [],
            "dataType": "String",
        },
        "bcc_emails": {
            "stringValue": "[]",
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
        "email_payload": {
            "stringValue": "{'value_in_usd': '$53,970.21', 'value_in_vnd': 'VND1,325,238,385', 'capital_usd_deployed': '$56,207.00', 'capital_vnd_deployed': 'VND1,380,161,435', 'stables_amount': 2372.44206021, 'stables_amount_vnd': 'VND58,255,315', 'PNL': {'pnl_in_vnd': '96.98%', 'pnl_in_usd': '92.13%', 'position_pnl_usd': '91.80%', 'position_pnl_vnd': '91.80%'}, 'current_usd_price': 24555.0, 'current_assets': {'totalAmountInBTC': '1.54658503', 'totalAmountInUSDT': '53970.20506937', 'totalFixedAmountInBTC': '0', 'totalFixedAmountInUSDT': '0', 'totalFlexibleInBTC': '1.54658503', 'totalFlexibleInUSDT': '53970.20506937', 'positionAmountVos': [{'asset': 'LINK', 'amount': '3995.18103052', 'amountInBTC': '1.47861649', 'amountInUSDT': '51597.76300916'}, {'asset': 'USDT', 'amount': '2372.44206021', 'amountInBTC': '0.06796854', 'amountInUSDT': '2372.44206021'}, {'asset': 'BTC', 'amount': '0', 'amountInBTC': '0', 'amountInUSDT': '0'}, {'asset': 'C98', 'amount': '0', 'amountInBTC': '0', 'amountInUSDT': '0'}, {'asset': 'ETH', 'amount': '0', 'amountInBTC': '0', 'amountInUSDT': '0'}, {'asset': 'BUSD', 'amount': '0', 'amountInBTC': '0', 'amountInUSDT': '0'}]}, 'deposits': {'capital_usd': 58579.38302743, 'capital_vnd': 1366444840.9069998, 'average_capital_price': 23326, 'total_buy_usd': 61322.81302743, 'total_buy_vnd': 1430942345.057, 'total_sell_usd': 2743.43, 'total_sell_vnd': 64497504.15, 'average_buy_price': 23334, 'average_sell_price': 23509}, 'link_price': 12.9, 'link_price_breakevent': 14.1, 'link_position_value': 51598, 'link_position_amount': 3995.18103052, 'current_statable_assets': '53970.20506937', 'deposit_usd': '$58,579.38', 'deposit_vnd': '$1,366,444,840.91', 'average_buy_price': 'VND23,334'}",
            "stringListValues": [],
            "binaryListValues": [],
            "dataType": "String",
        },
    },
    "md5OfMessageAttributes": "692a85a77642d77c6a669292b9512f66",
    "md5OfBody": "b84a406a1e74303f627f4a1242557bdd",
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
    res = _handle_sqs_email(email_template_fixture)

    assert res == True
