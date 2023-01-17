import boto3
from chalicelib.config import settings

ses = boto3.client("ses")

SES_FROM_ADDRESS = "tranthanhbao2207@gmail.com"


def get_new_otp_message(code):
    return (
        {
            "Body": {
                "Html": {
                    "Charset": "UTF-8",
                    "Data": "<html><body><p>This is your secret login code:</p>"
                    f"<h3>{code}</h3></body></html>",
                },
                "Text": {"Charset": "UTF-8", "Data": f"Your secret login code: {code}"},
            },
            "Subject": {"Charset": "UTF-8", "Data": "Your secret login code"},
        },
    )


def send_email(email, message: dict):
    ses.send_email(
        Source=SES_FROM_ADDRESS, Destination={"ToAddresses": [email]}, Message=message
    )
