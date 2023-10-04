from chalicelib.logger_app import logger

from .auth_listener import setup_auth_event_handlers
from .email_listener import setup_email_event_handlers
from .log_listener import setup_log_event_handlers


def init_listeners():
    setup_log_event_handlers()
    setup_email_event_handlers()
    setup_auth_event_handlers()
    logger.info("init listensers")
