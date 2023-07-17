# from chalicelib.blueprint import sns_bp
from chalice import Blueprint
from chalice.app import SNSEvent
from chalicelib.config import settings
from chalicelib.logger_app import logger
from chalicelib.events.base import EventType, subscribe_lambda_subscribers, subscribe
from chalicelib.logger_app import logger

import json

sns_bp = Blueprint(__name__)


@sns_bp.on_sns_message(topic=settings.SNS_MAIN_TOPIC_NAME)
def sns_base_handler(event: SNSEvent):
    """will receive all message from sns"""
    logger.info("sns_base_handlers")
    event_dict = event.to_dict()
    logger.info(
        "Received message with subject: {}, message: {}".format(
            event.subject,
            event.message,
        ),
    )
    print(type(event))
    logger.info(json.dumps(event_dict))


@sns_bp.on_sns_message(
    topic=settings.SNS_MAIN_TOPIC_NAME,
    name="KycoSnsPostSignupHandler",
)
def sns_post_signup_handler(event: SNSEvent):
    """will receive all message from sns"""
    logger.info(f"User {user} logged in successfully ! ")
    logger.info(event)


@sns_bp.on_sns_message(
    topic=settings.SNS_MAIN_TOPIC_NAME,
    name="KycoSnsPostSigninHandler",
)
def sns_post_signin_handler(event: SNSEvent):
    """will receive all message from sns"""
    logger.info(f"User {user}   in successfully ! ")
    logger.info(event)


def setup_sns_event_handlers():
    subscribe_lambda_subscribers(
        EventType.POST_USER_LOGIN,
        # sns_post_signin_handler,
        "KycoSnsPostSigninHandler",
    )

    subscribe_lambda_subscribers(
        EventType.POST_USER_REGISTER,
        # sns_post_signup_handler,
        "KycoSnsPostSignupHandler",
    )
