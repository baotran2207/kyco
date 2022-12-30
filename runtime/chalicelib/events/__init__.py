from chalicelib.logger_app import logger

from .event_type import EventType

subscribers = dict()


def subscribe(event_type: str, fn):
    if event_type not in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(fn)


def post_event(event_type: str, payload):
    if event_type not in subscribers:
        logger.info(
            f"EventType {event_type} is not in subscribers , does not have any listener! Doing nothing !"
        )
        return
    for fn in subscribers[event_type]:
        fn(payload)


def init_listeners():

    from .listener.email_listener import setup_email_event_handlers
    from .listener.log_listener import setup_log_event_handlers
    from .listener.users_listener import setup_user_event_handlers

    setup_log_event_handlers()
    setup_email_event_handlers()
    setup_user_event_handlers()
    print("listener")
    logger.info("init listensers")
