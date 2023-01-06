from chalicelib.events.base import EventType, subscribe
from chalicelib.logger_app import logger
from chalicelib.services.sqs_service import send_email_queue, parse_dict_to_sqs_message_attrs
from chalicelib.schemas.messages import SQSMESSAGE

def handle_user_registered_event(user):
    logger.info(f"Attemp to sync user with sql {user.dict()}")
    # message_attributes = parse_dict_to_sqs_message_attrs(user.dict())
    # send_email_queue("handle_post_user_login_event", message_attributes)


def handle_user_password_forgotten_event(user):
    logger.info(f"User with email address {user.username} requested a password reset")


def handle_user_upgrade_plan_event(user):
    logger.info(f"User with email address {user.username} has upgraded their plan")


def handle_post_user_login_event(user):
    logger.info(f"User login {user.dict()}")
    message_attributes = parse_dict_to_sqs_message_attrs(user.dict())
    send_email_queue("handle_post_user_login_event", message_attributes)
    logger.info(f"Send message ")

def setup_email_event_handlers():
    subscribe(EventType.POST_USER_REGISTER, handle_user_registered_event)
    subscribe(EventType.POST_USER_LOGIN, handle_post_user_login_event)
    # subscribe("user_password_forgotten", handle_user_password_forgotten_event)
    # subscribe("user_upgrade_plan", handle_user_upgrade_plan_event)
