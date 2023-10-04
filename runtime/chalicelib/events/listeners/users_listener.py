# import os

# from chalicelib.db.session import SessionLocal
# from chalicelib.events.base import EventType, post_event, subscribe
# from chalicelib.logger_app import logger
# from chalicelib.models import User
# from chalicelib.schemas.events import Subscriber as SubscriberSchema
# from chalicelib.schemas.user import UserCreate

# listener_group_name = os.path.basename(__file__)


# def handle_user_signup_event(user):
#     # session = SessionLocal()
#     # db_user = session.query(User.email == user.username).first()
#     # if db_user is None:
#     # new_db_user = User(**user.dict())
#     # session.add(new_db_user)
#     # session.commit()
#     logger.info(f"Attemp to add new user to remote sql db  {user}")


# def handler_user_cognito_signup_event(user):
#     logger.info(f"Attemp to add new user to cognito  {user}")


# def handler_post_sign_up_event(user):
#     logger.info(f"User {user} logged in successfully ! ")


# def handler_post_sign_in_event(user):
#     logger.info(f"User {user} logged in successfully ! ")


# def setup_user_event_handlers():
#     hanlders = {
#         EventType.POST_USER_REGISTER: handler_post_sign_up_event,
#         EventType.POST_USER_LOGIN: handler_post_sign_in_event,
#         # EventType.USER_PASSWORD_FORGOTTEN: handle_user_password_forgotten_event,
#     }

#     for event_type, handler in hanlders.items():
#         sub = SubscriberSchema(
#             event_type=event_type, fn=handler, listener_group_name=listener_group_name
#         )
#         subscribe(sub)

#     logger.info(f"Successfully setup {listener_group_name} handlers")
