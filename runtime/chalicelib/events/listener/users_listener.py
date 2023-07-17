from chalicelib.db.session import SessionLocal
from chalicelib.events.base import EventType, subscribe
from chalicelib.logger_app import logger
from chalicelib.models import User
from chalicelib.schemas.user import UserCreate


def handle_user_signup_event(user):
    print(f"User registered with email address {user}")
    # session = SessionLocal()
    # db_user = session.query(User.email == user.username).first()
    # if db_user is None:
    # new_db_user = User(**user.dict())
    # session.add(new_db_user)
    # session.commit()
    logger.info(f"Attemp to add new user to remote sql db  {user}")


def handler_user_cognito_signup_event(user):
    logger.info(f"Attemp to add new user to cognito  {user}")


def setup_user_event_handlers():
    subscribe(EventType.POST_USER_REGISTER, handle_user_signup_event)
    # subscribe("user_password_forgotten", handle_user_password_forgotten_event)
    # subscribe("user_upgrade_plan", handle_user_upgrade_plan_event)
