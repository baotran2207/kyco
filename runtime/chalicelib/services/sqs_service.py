from typing import Optional

import boto3
from botocore.exceptions import ClientError
from chalicelib.config import settings
from chalicelib.logger_app import logger

# from chalicelib.schemas.messages import SQSMESSAGE

sqs = boto3.resource("sqs")
# snippet-end:[python.example_code.sqs.message_wrapper_imports]


def check_queue_name(queue_name: str):
    if "arn:aws:sqs" not in queue_name:
        return queue_name
    return queue_name.split(":")[-1]


def get_queue(name: str):
    """
    Gets an SQS queue by name.
    :param name: The name that was used to create the queue.
    :return: A Queue object.
    """
    q_name = check_queue_name(name)
    try:
        queue = sqs.get_queue_by_name(QueueName=q_name)
        logger.info("Got queue '%s' with URL=%s", q_name, queue.url)
    except ClientError as error:
        logger.exception("Couldn't get queue named %s.", q_name)
        raise error
    else:
        return queue


# snippet-start:[python.example_code.sqs.SendMessage]
def send_message(queue, message_body: str, message_attributes: Optional[dict] = None):
    """
    Send a message to an Amazon SQS queue.
    :param queue: The queue that receives the message.
    :param message_body: The body text of the message.
    :param message_attributes: Custom attributes of the message. These are key-value
                               pairs that can be whatever you want.
    :return: The response from SQS that contains the assigned message ID.
    """
    if not message_attributes:
        message_attributes = {}
    try:
        response = queue.send_message(
            MessageBody=message_body, MessageAttributes=message_attributes
        )
        logger.info("Sent message: %s", message_body)
    except ClientError as error:
        logger.exception("Send message failed: %s", message_body)
        raise error
    else:
        return response


# snippet-end:[python.example_code.sqs.SendMessage]


# snippet-start:[python.example_code.sqs.SendMessageBatch]
def send_messages(queue, messages):
    """
    Send a batch of messages in a single request to an SQS queue.
    This request may return overall success even when some messages were not sent.
    The caller must inspect the Successful and Failed lists in the response and
    resend any failed messages.
    :param queue: The queue to receive the messages.
    :param messages: The messages to send to the queue. These are simplified to
                     contain only the message body and attributes.
    :return: The response from SQS that contains the list of successful and failed
             messages.
    """
    try:
        entries = [
            {
                "Id": str(ind),
                "MessageBody": msg["body"],
                "MessageAttributes": msg["attributes"],
            }
            for ind, msg in enumerate(messages)
        ]
        response = queue.send_messages(Entries=entries)
        if "Successful" in response:
            for msg_meta in response["Successful"]:
                logger.info(
                    "Message sent: %s: %s",
                    msg_meta["MessageId"],
                    messages[int(msg_meta["Id"])]["body"],
                )
        if "Failed" in response:
            for msg_meta in response["Failed"]:
                logger.warning(
                    "Failed to send: %s: %s",
                    msg_meta["MessageId"],
                    messages[int(msg_meta["Id"])]["body"],
                )
    except ClientError as error:
        logger.exception("Send messages failed to queue: %s", queue)
        raise error
    else:
        return response


def send_email_queue(message_body: str, message_attributes: Optional[dict] = None):
    sqs_email = get_queue(settings.SQS_SENDEMAIL)
    sqs_message_attributes = parse_dict_to_sqs_message_attrs(message_attributes)
    logger.info(f"Sending message to sqs {message_body} ")
    return send_message(sqs_email, message_body, sqs_message_attributes)


def parse_dict_to_sqs_message_attrs(dict_: dict) -> dict:
    return {key: {"StringValue": str(val), "DataType": "String"} for key, val in dict_.items()}


def parse_sqs_message_attrs_to_dict(sqs_message_attrs: dict[str:dict]) -> dict[str:str]:
    res = {}
    for key, val in sqs_message_attrs.items():
        res[key] = val.get("StringValue") or val.get("stringValue")
    return res


def delete_messages(queue, messages):
    """
    Delete a batch of messages from a queue in a single request.

    :param queue: The queue from which to delete the messages.
    :param messages: The list of messages to delete.
    :return: The response from SQS that contains the list of successful and failed
             message deletions.
    """
    try:
        entries = [
            {
                "Id": str(ind),
                "ReceiptHandle": msg.receipt_handle,
            }
            for ind, msg in enumerate(messages)
        ]
        response = queue.delete_messages(Entries=entries)
        if "Successful" in response:
            for msg_meta in response["Successful"]:
                logger.info("Deleted %s", messages[int(msg_meta["Id"])].receipt_handle)
        if "Failed" in response:
            for msg_meta in response["Failed"]:
                logger.warning("Could not delete %s", messages[int(msg_meta["Id"])].receipt_handle)
    except ClientError:
        logger.exception("Couldn't delete messages from queue %s", queue)
    else:
        return response
