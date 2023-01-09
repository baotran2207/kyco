from chalice import Blueprint
from chalice.app import SQSEvent, SQSRecord
from chalicelib.config import settings
from chalicelib.logger_app import logger

sqs_bp = Blueprint(__name__)

"""
{'Records':
    [{
        'messageId': '3713e86a-9204-4fcf-a4e0-a2ac8d5a7d60',
        'receiptHandle': 'AQEB4dzu0n+Z0ow8RCJUW0AuFiMaNbvvDTQHuwbHTVjVhTdWFGTHf8Rh6EBb7EumykBQuhc+0jzdhtYxlKqbIv4uknkHFvgP+X8oJHcMk5798dbUBBe9GO6o0z+3idG/JmzNBzvoFbIWUTYNZvOsh59+TTdr/CHXHfOurw+43BLM9UKazCLBjcZYI7p3O4l/gy2K0uo0Iq4ieI8LbRaqArlIqO7v90N2y8GDuxDV0rhvpQlzzivaZAH9XCydmob8N5bkFajDGDYb21H7LI0bG+0j6rYsnk5PbWfvcGyJrvacE+O5anu4TgcjH/Du4+jhVqkmnM4rxziaqaxUU6ojsOYzBKOaEPVoxVwN15V/Kken/7CRDw0ezwnE9PK+5MjN6Y99GomKwVlFfLGw82HJnpN+WA==',
        'body': 'test sqs mesg',
        'attributes': {
            'ApproximateReceiveCount': '1', 'AWSTraceHeader': 'Root=1-63b796bd-3d4d8f371599871c08850c42;Parent=21f6f6d55f3c05d2;Sampled=0',
            'SentTimestamp': '1672976064184',
            'SenderId': 'AROA2UDD5TARNC7GJDOXE:kyco-chalice-id-APIHandler-2IvMdGeLzzNJ',
            'ApproximateFirstReceiveTimestamp': '1672976064191'
        },
        'messageAttributes': {
            'path': {'stringValue': 'test', 'stringListValues': [], 'binaryListValues': [], 'dataType': 'String'},
            'line': {'stringValue': 'trigger', 'stringListValues': [], 'binaryListValues': [], 'dataType': 'String'}
        },
            'md5OfMessageAttributes': 'fcd02f200ceb59c5ed5c9b00962fa92b', 'md5OfBody': '16b90106d00f6ef6a023eff45ca82774', 'eventSource': 'aws:sqs', 'eventSourceARN': 'arn:aws:sqs:ap-southeast-1:730353997858:KycoGeneric', 'awsRegion': 'ap-southeast-1'}]}

"""


@sqs_bp.on_sqs_message(queue_arn=settings.SQS_GENERIC, batch_size=10)
def handle_sqs_generic(event: SQSEvent):
    for record in event:
        body = record.body
        print(body)
        logger.info(f" in even ! Detail {record} ")
        print(record.messageAttributes)


@sqs_bp.on_sqs_message(queue_arn=settings.SQS_SENDEMAIL, batch_size=1)
def handle_sqs_email(event: SQSEvent):
    for record in event:
        logger.info(f" record: {record.body} ")
        logger.info(f" record dict {record.dict()} ")
        logger.info(f" record dict {record.messageAttributes} ")
