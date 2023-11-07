import json
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from .emails import EmailMessage, EmailTemplatedMessage

#  computed_field


class Msg(BaseModel):
    msg: str


class SQSMessage(BaseModel):
    message: dict


#     @property
#     def sub_msg(self) -> dict:
#         return json.loads(self.message["Message"])

#     @computed_field
#     @property
#     def message_id(self) -> str:
#         return self.message["MessageId"]

#     @computed_field
#     @property
#     def event_datetime(self) -> datetime:
#         _dt = self.sub_msg["Records"][0]["eventTime"]
#         if "Z" in _dt:
#             return datetime.fromisoformat(self.sub_msg["Records"][0]["eventTime"].replace("Z", ""))
#         else:
#             return datetime.fromisoformat(self.sub_msg["Records"][0]["eventTime"])


# class EmailSqsMessage(SQSMessage):
#     @computed_field
#     @property
#     def is_templated_message(self) -> bool:
#         return "template_name" in self.message["MessageAttributes"]

#     @computed_field
#     @property
#     def email_message(self) -> EmailMessage | EmailTemplatedMessage:
#         if self.is_templated_message:
#             return EmailTemplatedMessage(**self.message["MessageAttributes"])
#         else:
#             return EmailMessage(**self.message["MessageAttributes"])
