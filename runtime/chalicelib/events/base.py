from chalicelib.logger_app import logger
from .event_type import EventType
from chalicelib.services.sns_service import (
    publish_message,
    sns_wrapper,
    topic as sns_topic,
)
import json
from itertools import chain

subscribers = dict()
lambda_subscribers = dict()


def subscribe(event_type: str, fn):
    if event_type not in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(fn)


def unsubscribe(event_type: str, fn):
    if event_type not in subscribers:
        return
    subscribers = [event for event in subscribers if event != event_type]


def subscribe_lambda_subscribers(event_type: str, lambda_name: str):
    if event_type not in lambda_subscribers:
        lambda_subscribers[event_type] = []
    lambda_subscribers[event_type].append(lambda_name)


def post_event(event_type: str, payload: dict):
    if event_type not in subscribers:
        logger.info(
            "EventType {} is not in subscribers , does not have any listener!".format(
                event_type,
            ),
        )
        return
    for fn in subscribers[event_type]:
        fn(payload)

    for lambda_name in lambda_subscribers[event_type]:
        message_attributes = {
            "lambda_name": lambda_name,
            "payload": json.dumps(payload),
        }
        message_body = (
            "message" in payload and payload["message"] or "message is not defined"
        )
        publish_message(message=message_body, attributes=message_attributes)


def init_listeners():
    from .listener.email_listener import setup_email_event_handlers
    from .listener.log_listener import setup_log_event_handlers
    from .listener.users_listener import setup_user_event_handlers
    from chalicelib.events.v1.sns_events import setup_sns_event_handlers

    setup_log_event_handlers()
    setup_email_event_handlers()
    setup_user_event_handlers()
    logger.info("init listensers")

    setup_sns_event_handlers()
    logger.info("init sns subscribers")


# this is post deployment event
def add_filters_to_lambda_subscribers():
    topic_subs = sns_wrapper.list_subscriptions_by_topic(sns_topic.arn)
    for lambda_name in chain(*lambda_subscribers.values()):
        logger.debug(lambda_name)
        lambda_endpoints_sub = [
            sub for sub in topic_subs if lambda_name in str(sub["Endpoint"])
        ]
        if not lambda_endpoints_sub:
            continue
        for sub in lambda_endpoints_sub:
            res = sns_wrapper.set_subscription_filter_policy(
                subscription_arn=sub["SubscriptionArn"],
                filter_policy={"lambda_name": [lambda_name]},
            )
            logger.debug(res)
