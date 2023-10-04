import json
from collections import defaultdict
from itertools import chain

from chalicelib.config import settings
from chalicelib.enums import AppEnv
from chalicelib.logger_app import logger
from chalicelib.schemas.events import Subscriber as SubscriberSchema
from chalicelib.services.sns_service import publish_message, sns_wrapper
from chalicelib.services.sns_service import topic as sns_topic

from .event_type import EventType

subscribers = defaultdict()
lambda_subscribers = dict()


def subscribe(subscriber: SubscriberSchema):
    event_type = subscriber.event_type
    function_name = subscriber.fn.__name__
    listener_group_name = subscriber.listener_group_name
    if subscriber.event_type not in subscribers:
        subscribers[subscriber.event_type] = []
    subscribers[subscriber.event_type].append(subscriber.fn)
    logger.debug(f"Subscribe {listener_group_name} - {function_name}  to {event_type} ")


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
        message_body = payload
        message_attributes = {"event_type": event_type}
        logger.debug(message_body)
        # if settings.ENV == AppEnv.dev.value:
        #     fn(payload)
        # else:
        publish_message(message=json.dumps(message_body), attributes=message_attributes)


# def init_listeners():
#     from chalicelib.events.v1.sns_events import setup_sns_event_handlers

#     from .listener.email_listener import setup_email_event_handlers
#     from .listener.log_listener import setup_log_event_handlers
#     from .listener.users_listener import setup_user_event_handlers

#     setup_log_event_handlers()
#     setup_email_event_handlers()
#     setup_user_event_handlers()
#     logger.info("init listensers")

#     setup_sns_event_handlers()
#     logger.info("init sns subscribers")


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
