from dataclasses import dataclass


@dataclass(frozen=True)
class EventType:
    POST_USER_REGISTER = "POST_USER_REGISTER"
    PRE_USER_REGISTER = "PRE_USER_REGISTER"

    USER_REGISTER = "USER_REGISTER"
    USER_REGISTER_COGNITO = "USER_REGISTER_COGNITO"

    POST_USER_LOGIN = "POST_USER_LOGIN"
    PRE_USER_LOGIN = "PRE_USER_LOGIN"
