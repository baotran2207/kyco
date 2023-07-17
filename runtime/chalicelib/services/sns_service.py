"""
ref: https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/sns
"""

import json
import time

import boto3
from botocore.exceptions import ClientError
from chalicelib.config import settings
from chalicelib.logger_app import logger

MAIN_TOPIC = settings.SNS_MAIN_TOPIC_NAME
MAIN_TOPIC_ARN = settings.SNS_MAIN_TOPIC_ARN


class SnsWrapper:
    """Encapsulates Amazon SNS topic and subscription functions."""

    def __init__(self, sns_resource, sns_client):
        """
        :param sns_resource: A Boto3 Amazon SNS resource.
        """
        self.sns_resource = sns_resource
        self.sns_client = sns_client

    # snippet-end:[python.example_code.sns.SnsWrapper]

    # snippet-start:[python.example_code.sns.CreateTopic]
    def create_topic(self, topic_arn):
        """
        Creates a notification topic.

        :param name: The name of the topic to create.
        :return: The newly created topic.
        """
        try:
            topic = self.sns_resource.Topic(topic_arn)
            logger.info("Connected topic ARN %s.", topic_arn)
        except ClientError:
            logger.exception("Couldn't create topic %s.", topic_arn)
            raise
        else:
            return topic

    # snippet-end:[python.example_code.sns.CreateTopic]

    # snippet-start:[python.example_code.sns.ListTopics]
    def list_topics(self):
        """
        Lists topics for the current account.

        :return: An iterator that yields the topics.
        """
        try:
            topics_iter = self.sns_resource.topics.all()
            logger.info("Got topics.")
        except ClientError:
            logger.exception("Couldn't get topics.")
            raise
        else:
            return topics_iter

    # snippet-end:[python.example_code.sns.ListTopics]

    @staticmethod
    # snippet-start:[python.example_code.sns.DeleteTopic]
    def delete_topic(topic):
        """
        Deletes a topic. All subscriptions to the topic are also deleted.
        """
        ...

    # snippet-end:[python.example_code.sns.DeleteTopic]

    @staticmethod
    # snippet-start:[python.example_code.sns.Subscribe]
    def subscribe(topic, protocol, endpoint):
        """
        Subscribes an endpoint to the topic. Some endpoint types, such as email,
        must be confirmed before their subscriptions are active. When a subscription
        is not confirmed, its Amazon Resource Number (ARN) is set to
        'PendingConfirmation'.

        :param topic: The topic to subscribe to.
        :param protocol: The protocol of the endpoint, such as 'sms' or 'email'.
        :param endpoint: The endpoint that receives messages, such as a phone number
                         (in E.164 format) for SMS messages, or an email address for
                         email messages.
        :return: The newly added subscription.
        """
        try:
            subscription = topic.subscribe(
                Protocol=protocol,
                Endpoint=endpoint,
                ReturnSubscriptionArn=True,
            )
            logger.info(
                "Subscribed %s %s to topic %s.",
                protocol,
                endpoint,
                topic.arn,
            )
        except ClientError:
            logger.exception(
                "Couldn't subscribe %s %s to topic %s.",
                protocol,
                endpoint,
                topic.arn,
            )
            raise
        else:
            return subscription

    # snippet-end:[python.example_code.sns.Subscribe]

    # snippet-start:[python.example_code.sns.ListSubscriptions]
    def list_subscriptions(self, topic=None):
        """
        Lists subscriptions for the current account, optionally limited to a
        specific topic.

        :param topic: When specified, only subscriptions to this topic are returned.
        :return: An iterator that yields the subscriptions.
        """
        try:
            if topic is None:
                subs_iter = self.sns_resource.subscriptions.all()
            else:
                subs_iter = topic.subscriptions.all()
            logger.info("Got subscriptions.")
        except ClientError:
            logger.exception("Couldn't get subscriptions.")
            raise
        else:
            return subs_iter

    def list_subscriptions_by_topic(self, topic_arn=None):
        """
        Lists subscriptions for the current account, optionally limited to a
        specific topic.

        :param topic: When specified, only subscriptions to this topic are returned.
        :return: An iterator that yields the subscriptions.
        """

        try:
            subs_iter = self.sns_client.list_subscriptions_by_topic(
                TopicArn=topic_arn,
            )
            logger.info("Got endpoints.")
        except ClientError:
            logger.exception("Couldn't get endpoints.")
            raise
        else:
            return subs_iter["Subscriptions"]

    # snippet-end:[python.example_code.sns.ListSubscriptions]

    @staticmethod
    # snippet-start:[python.example_code.sns.Unsubscribe]
    def delete_subscription(subscription):
        """
        Unsubscribes and deletes a subscription.
        """
        try:
            subscription.delete()
            logger.info("Deleted subscription %s.", subscription.arn)
        except ClientError:
            logger.exception("Couldn't delete subscription %s.", subscription.arn)
            raise

    # snippet-end:[python.example_code.sns.Unsubscribe]

    # snippet-start:[python.example_code.sns.Publish_TextMessage]
    def publish_text_message(self, phone_number, message):
        """
        Publishes a text message directly to a phone number without need for a
        subscription.

        :param phone_number: The phone number that receives the message. This must be
                             in E.164 format. For example, a United States phone
                             number might be +12065550101.
        :param message: The message to send.
        :return: The ID of the message.
        """
        try:
            response = self.sns_resource.meta.client.publish(
                PhoneNumber=phone_number, Message=message
            )
            message_id = response["MessageId"]
            logger.info("Published message to %s.", phone_number)
        except ClientError:
            logger.exception("Couldn't publish message to %s.", phone_number)
            raise
        else:
            return message_id

    # snippet-end:[python.example_code.sns.Publish_TextMessage]

    @staticmethod
    # snippet-start:[python.example_code.sns.Publish_MessageAttributes]
    def publish_message(topic, message, attributes):
        """
        Publishes a message, with attributes, to a topic. Subscriptions can be filtered
        based on message attributes so that a subscription receives messages only
        when specified attributes are present.

        :param topic: The topic to publish to.
        :param message: The message to publish.
        :param attributes: The key-value attributes to attach to the message. Values
                           must be either `str` or `bytes`.
        :return: The ID of the message.
        """
        try:
            att_dict = {}
            for key, value in attributes.items():
                if isinstance(value, str):
                    att_dict[key] = {"DataType": "String", "StringValue": value}
                elif isinstance(value, bytes):
                    att_dict[key] = {"DataType": "Binary", "BinaryValue": value}
            response = topic.publish(Message=message, MessageAttributes=att_dict)
            message_id = response["MessageId"]
            logger.info(
                "Published message %s with attributes %s to topic %s. ",
                message,
                attributes,
                topic.arn,
            )
        except ClientError:
            logger.exception("Couldn't publish message to topic %s.", topic.arn)
            raise
        else:
            return message_id

    # snippet-end:[python.example_code.sns.Publish_MessageAttributes]

    def set_subscription_attributes(self, subscription_arn, attributes):
        """
        Sets the attributes of a subscription.

        :param subscription_arn: The ARN of the subscription.
        :param attributes: A dictionary of key-value pairs that define the attributes.
        """
        try:
            self.sns_client.set_subscription_attributes(
                SubscriptionArn=subscription_arn, AttributeName=attributes
            )
            logger.info("Set attributes for subscription %s.", subscription_arn)
        except ClientError:
            logger.exception(
                "Couldn't set attributes for subscription %s.", subscription_arn
            )
            raise

    def set_subscription_filter_policy(self, subscription_arn, filter_policy):
        """
        Sets the filter policy of a subscription.

        :param subscription_arn: The ARN of the subscription.
        :param filter_policy: A dictionary of key-value pairs that define the filter.
        """
        try:
            self.sns_client.set_subscription_attributes(
                SubscriptionArn=subscription_arn,
                AttributeName="FilterPolicy",
                AttributeValue=json.dumps(filter_policy),
            )
            logger.info(
                "Set filter policy for subscription {} with {}.".format(
                    subscription_arn, json.dumps(filter_policy)
                )
            )
        except ClientError:
            logger.exception(
                "Couldn't set filter policy for subscription %s.", subscription_arn
            )
            raise

    @staticmethod
    # snippet-start:[python.example_code.sns.Publish_MessageStructure]
    def publish_multi_message(
        topic, subject, default_message, sms_message, email_message
    ):
        """
        Publishes a multi-format message to a topic. A multi-format message takes
        different forms based on the protocol of the subscriber. For example,
        an SMS subscriber might receive a short, text-only version of the message
        while an email subscriber could receive an HTML version of the message.

        :param topic: The topic to publish to.
        :param subject: The subject of the message.
        :param default_message: The default version of the message. This version is
                                sent to subscribers that have protocols that are not
                                otherwise specified in the structured message.
        :param sms_message: The version of the message sent to SMS subscribers.
        :param email_message: The version of the message sent to email subscribers.
        :return: The ID of the message.
        """
        try:
            message = {
                "default": default_message,
                "sms": sms_message,
                "email": email_message,
            }
            response = topic.publish(
                Message=json.dumps(message), Subject=subject, MessageStructure="json"
            )
            message_id = response["MessageId"]
            logger.info("Published multi-format message to topic %s.", topic.arn)
        except ClientError:
            logger.exception("Couldn't publish message to topic %s.", topic.arn)
            raise
        else:
            return message_id


sns_wrapper = SnsWrapper(boto3.resource("sns"), boto3.client("sns"))
topic = sns_wrapper.create_topic(MAIN_TOPIC_ARN)


def publish_message(message: str, attributes: dict):
    sns_wrapper.publish_message(
        topic,
        message,
        attributes,
    )


if __name__ == "__main__":
    usage_demo()
