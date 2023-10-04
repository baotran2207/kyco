# from chalicelib.blueprint import sns_bp
import json

from chalice import Blueprint
from chalice.app import SNSEvent
from chalicelib.config import settings
from chalicelib.events.base import (
    EventType,
    subscribe,
    subscribe_lambda_subscribers,
    subscribers,
)
from chalicelib.logger_app import logger

sns_bp = Blueprint(__name__)


@sns_bp.on_sns_message(topic=settings.SNS_MAIN_TOPIC_NAME)
def sns_base_handler(event: SNSEvent):
    """will receive all message from sns"""
    logger.info("sns_base_handlers")
    event_payload = event.message
    message_attributes = event.message_attributes
    event_type = message_attributes.get("event_type").get("Value")

    event_dict = event.to_dict()
    # event_type = event_dict.get("event_type")
    # event_payload = event_dict.get("payload")

    logger.info(
        "Received message with subject: {}, message: {}".format(
            event.subject,
            event.message,
        ),
    )

    if event_type not in subscribers:
        logger.info(f"Event type - {event_type} - is not supported")
        return

    for fn in subscribers[event_type]:
        logger.info(f"Executing event_type: {event_type} ; function : {fn.__name__}")
        fn(event_payload)

    logger.info(f"Successfully executed event_type: {event_type} ")


# @sns_bp.on_sns_message(
#     topic=settings.SNS_MAIN_TOPIC_NAME,
#     name="KycoSnsPostSigninHandler",
# )
# def sns_post_signin_handler(event: SNSEvent):
#     """will receive all message from sns"""
#     event_dict = event.to_dict()
#     logger.info(f"User {json.dumps(event_dict)}   in successfully ! ")
#     logger.info(event)


# def setup_sns_event_handlers():
#     subscribe_lambda_subscribers(
#         EventType.POST_USER_LOGIN,
#         # sns_post_signin_handler,
#         "KycoSnsPostSigninHandler",
#     )

#     subscribe_lambda_subscribers(
#         EventType.POST_USER_REGISTER,
#         # sns_post_signup_handler,
#         "KycoSnsPostSignupHandler",
#     )
