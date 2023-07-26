from dataclasses import dataclass
from typing import Protocol

from botocore.exceptions import ClientError
from chalicelib.events.base import EventType, post_event
from chalicelib.logger_app import logger
from chalicelib.schemas import UserCreate, UserSignIn
from chalicelib.services.authorizers import Authenticator
from chalicelib.services.authorizers import authenticator as current_authenticator


class Users(Protocol):
    def create(self, user: UserCreate):
        ...

    def update(self, user: UserCreate):
        ...

    def delete(self, user: UserCreate):
        ...

    def get(self, user: UserCreate):
        ...

    def get_users(self):
        ...
