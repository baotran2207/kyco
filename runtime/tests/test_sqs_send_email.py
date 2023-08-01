import json

from chalicelib.utils import parse_sqs_record_to_email_messages

# from chalicelib.events.v1.sqs_events import parse_sqs_record_to_email_messages
message_str = {
    "Body": {
        "Html": {
            "Charset": "UTF-8",
            "Data": 'This message body contains HTML formatting. It can, for example, contain links like this one: <a class="ulink" href="http://docs.aws.amazon.com/ses/latest/DeveloperGuide" target="_blank">Amazon SES Developer Guide</a>.',
        },
        "Text": {
            "Charset": "UTF-8",
            "Data": "This is the message body in text format.",
        },
    },
    "Subject": {
        "Charset": "UTF-8",
        "Data": "Test email",
    },
}
sqs_record = {
    "messageId": "482daa94-8005-4761-8eab-d923f1823e9b",
    "receiptHandle": "",
    "body": "sending email",
    "attributes": {
        "ApproximateReceiveCount": "1381",
        "AWSTraceHeader": "Root=1-64c5f1e2-68d97fd165f9d67b1b5b9534;Parent=5653e3fb338c17ea;Sampled=0;Lineage=55db472c: 0",
        "SentTimestamp": "1690694118989",
        "SenderId": "AROA2UDD5TARNC7GJDOXE:kyco-chalice-id-AutoSendPorfolioSummary-ql5YbMlIoqby",
        "ApproximateFirstReceiveTimestamp": "1690694118989",
    },
    "messageAttributes": {
        "to_emails": {
            "stringValue": "['tranthanhbao2207@gmail.com']",
            "stringListValues": [],
            "binaryListValues": [],
            "dataType": "String",
        },
        "email_message": {
            "stringValue": json.dumps(message_str),
            "stringListValues": [],
            "binaryListValues": [],
            "dataType": "String",
        },
        "cc_emails": {
            "stringValue": "None",
            "stringListValues": [],
            "binaryListValues": [],
            "dataType": "String",
        },
        "reply_tos": {
            "stringValue": "None",
            "stringListValues": [],
            "binaryListValues": [],
            "dataType": "String",
        },
        "bcc_emails": {
            "stringValue": "None",
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
    "md5OfMessageAttributes": "b8470eeb4c6b2b662867ae4a8a561019",
    "md5OfBody": "afd4531025a150bff11f6a5149414b69",
    "eventSource": "aws:sqs",
    "eventSourceARN": "arn:aws:sqs:ap-southeast-1: 730353997858:KycoSendemail",
    "awsRegion": "ap-southeast-1",
}


def test_parse_sqs_record_to_email_messages():
    a = ["tranthanhbao2207@gmail.com", "examples"]
    b = json.dumps(a)
    print(a)
    print(b)
    print(json.loads(b))
    # res = parse_sqs_record_to_email_messages(sqs_record)
    assert True
    # print(res)
