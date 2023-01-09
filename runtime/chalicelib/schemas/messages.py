from typing import Optional

from pydantic import BaseModel


class Msg(BaseModel):
    msg: str


class SQSMESSAGE(BaseModel):
    message_body: str
    message_attributes: Optional[dict] = None
