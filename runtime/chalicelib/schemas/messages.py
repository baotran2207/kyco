from pydantic import BaseModel
from typing import Optional

class Msg(BaseModel):
    msg: str


class SQSMESSAGE(BaseModel):
    message_body: str
    message_attributes: Optional[dict] = None