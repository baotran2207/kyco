from chalicelib.events.base import EventType, post_event
from chalicelib.schemas import UserSignIn
from chalicelib.services.authorizers import Authenticator
from chalicelib.services.authorizers import authenticator as cog_authenticator


def login(user: UserSignIn, authenticator: Authenticator = cog_authenticator):
    response = authenticator.sign_in(user.username, user.password)
    post_event(EventType.POST_USER_LOGIN, user)
    return response
