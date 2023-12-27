import os
from dataclasses import dataclass
from typing import Optional

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


@dataclass
class EmailTemplate:
    template_name: str
    subject_part: str

    # the properties below are optional
    html_part: Optional[str] = ""
    text_part: Optional[str] = ""

    def __post_init__(self):
        template_name = self.template_name
        template_path = _get_email_template_path(template_name)
        with open(template_path, "r", encoding="utf-8") as f:
            text = f.read()
        self.html_part = text


NEW_OTP_TEMPLATE = EmailTemplate(
    template_name="NEW_OTP",
    subject_part="Your OTP code",
    html_part="",
    text_part="Your secret login code is : {{otp_code}}",
)


PORFOLIO_OVERVIEW_TEMPLATE = EmailTemplate(
    template_name="PORFOLIO_OVERVIEW",
    subject_part="Your portfolio overview",
    html_part="",
)

emails_templates = [
    NEW_OTP_TEMPLATE,
    PORFOLIO_OVERVIEW_TEMPLATE,
]
