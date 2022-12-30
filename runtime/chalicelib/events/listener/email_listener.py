from chalicelib.events import EventType, subscribe
from chalicelib.logger_app import logger


def handle_user_registered_event(user):
    print(user, logger.level)
    logger.info(f"User registered with email address {user.username}")


def handle_user_password_forgotten_event(user):
    logger.info(f"User with email address {user.username} requested a password reset")


def handle_user_upgrade_plan_event(user):
    logger.info(f"User with email address {user.username} has upgraded their plan")


def setup_email_event_handlers():
    subscribe(EventType.POST_USER_REGISTER, handle_user_registered_event)
    # subscribe("user_password_forgotten", handle_user_password_forgotten_event)
    # subscribe("user_upgrade_plan", handle_user_upgrade_plan_event)
