import ast
from typing import Optional

from pydantic import BaseModel, EmailStr, validator


class EmailMessage(BaseModel):
    to_emails: list
    email_payload: dict | str
    source: EmailStr
    cc_emails: Optional[list] = []
    bcc_emails: Optional[list] = []
    reply_tos: Optional[list] = []

    @validator("to_emails", pre=True, always=True)
    def validate_to_emails(cls, v):
        if v is None:
            return []
        if isinstance(v, list):
            return v
        res = ast.literal_eval(v)
        return res

    @validator("cc_emails", pre=True, always=True)
    def validate_cc_emails_payload(cls, v):
        if v is None:
            return []
        if isinstance(v, list):
            return v
        res = ast.literal_eval(v)
        return res

    @validator("bcc_emails", pre=True, always=True)
    def validate_bcc_emails(cls, v):
        if v is None:
            return []
        if isinstance(v, list):
            return v
        res = ast.literal_eval(v)
        return res

    @validator("reply_tos", pre=True, always=True)
    def validate_reply_tos_emails(cls, v):
        if v is None:
            return []
        if isinstance(v, list):
            return v
        res = ast.literal_eval(v)
        return res

    @validator("email_payload", pre=True, always=True)
    def validate_email_payload(cls, v):
        if v is None:
            return {}
        if isinstance(v, dict):
            return v
        res = ast.literal_eval(v)
        return res


class EmailTemplatedMessage(EmailMessage):
    template_name: str
