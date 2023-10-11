from typing import Optional

from pydantic import BaseModel, EmailStr


class Msg(BaseModel):
    msg: str


class SQSMESSAGE(BaseModel):
    message_body: str
    message_attributes: Optional[dict] = None


class EmailSqsMessage(BaseModel):
    to_emails: list
    email_payload: dict | str
    source: EmailStr
    template_name: Optional[str] = None
    email_type: Optional[str] = None
    cc_emails: Optional[list] = []
    bcc_emails: Optional[list] = []
    reply_tos: Optional[list] = []
