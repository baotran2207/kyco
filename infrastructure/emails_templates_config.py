import os
from typing import Optional

from pydantic import BaseModel, validator

PARRENT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")

print(
    os.path.dirname(os.path.dirname(__file__)),
)


def _get_email_template_path(template_name: str) -> str:
    return os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "static",
        "emails-template",
        f"{template_name}.html",
    )


class EmailTemplate(BaseModel):
    template_name: str
    subject_part: str

    # the properties below are optional
    html_part: Optional[str]
    text_part: Optional[str]

    @validator("html_part", each_item=True)
    def fetch_html_part(cls, v, values):
        template_name = values.get("template_name")
        if v:
            return v
        template_path = _get_email_template_path(template_name)
        with open(template_path, "r", encoding="utf-8") as f:
            text = f.read()
        return text


NEW_OTP_TEMPLATE = EmailTemplate(
    template_name="NEW_OTP",
    subject_part="Your OTP code",
    html_part="",
    text_part="Your secret login code is : {{otp_code}}",
)


PORFOLIO_OVERVIEW_TEMPLATE = EmailTemplate(
    template_name="PORFOLIO_OVERVIEW",
    subject_part="Your secret login code",
    html_part="",
)

emails_templates = [
    NEW_OTP_TEMPLATE,
    PORFOLIO_OVERVIEW_TEMPLATE,
]
