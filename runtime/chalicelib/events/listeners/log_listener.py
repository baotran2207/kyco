from chalicelib.events.base import EventType, subscribe
from chalicelib.logger_app import logger
from chalicelib.schemas.events import Subscriber as SubscriberSchema


def handle_user_registered_event(user):
    logger.info(f"Sending email {user}")


def handle_user_password_forgotten_event(user):
    logger.info(f"User with email address {user} requested a password reset")


def handle_user_upgrade_plan_event(user):
    logger.info(f"User with email address {user} has upgraded their plan")


def handle_post_user_login_event(payload):
    logger.info(f"User {payload} logged in successfully ! ")


def setup_log_event_handlers():
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
