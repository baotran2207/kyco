from chalicelib.events.base import EventType, subscribe
from chalicelib.logger_app import logger
from chalicelib.schemas.events import Subscriber as SubscriberSchema

# from chalicelib.schemas.messages import SQSMESSAGE
from chalicelib.services.sqs_service import (
    parse_dict_to_sqs_message_attrs,
    send_email_queue,
)


def handle_user_registered_event(user):
    logger.info(f"Attemp to sync user with sql {user}")
    # message_attributes = parse_dict_to_sqs_message_attrs(user.dict())
    # send_email_queue("handle_post_user_login_event", message_attributes)


def handle_user_password_forgotten_event(user):
    logger.info(f"User with email address {user} requested a password reset")


def handle_post_user_login_event(payload):
    logger.info(f"User login {payload}")
    # message_attributes = parse_dict_to_sqs_message_attrs(payload)
    # send_email_queue("handle_post_user_login_event", message_attributes)
    logger.info("Sent message ")


def handle_send_otp(payload: dict):
    pass
    # send sms by


def setup_email_event_handlers():
    # subscribe(EventType.POST_USER_REGISTER, handle_user_registered_event)
    # subscribe(EventType.POST_USER_LOGIN, handle_post_user_login_event)
    # # subscribe("user_password_forgotten", handle_user_password_forgotten_event)
    # # subscribe("user_upgrade_plan", handle_user_upgrade_plan_event)
    hanlders = {
        EventType.POST_USER_REGISTER: handle_user_registered_event,
        EventType.POST_USER_LOGIN: handle_post_user_login_event,
        # EventType.USER_PASSWORD_FORGOTTEN: handle_user_password_forgotten_event,
    }

    for event_type, handler in hanlders.items():
        sub = SubscriberSchema(
            event_type=event_type, fn=handler, listener_group_name=__file__
        )
        subscribe(sub)

    logger.info(f"Successfully setup {__file__} handlers")
