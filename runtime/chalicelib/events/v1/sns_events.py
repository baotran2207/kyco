# from chalicelib.blueprint import sns_bp
from chalice import Blueprint
from chalicelib.config import settings
from chalicelib.logger_app import logger

sns_bp = Blueprint(__name__)


@sns_bp.on_sns_message(topic=settings.SNS_MAIN_TOPIC_NAME)
def generic_handler(event):
    """will receive all message from sns"""
    print("generic_handler")
    print(event)
