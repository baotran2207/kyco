import boto3
from chalicelib.config import settings

ses = boto3.client("ses")

SES_FROM_ADDRESS = settings.WEBMASTER_EMAIL


def get_new_otp_message(code) -> dict:
    return dict(
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
    return ses.send_email(
        Source=SES_FROM_ADDRESS, Destination={"ToAddresses": [email]}, Message=message
    )


def send_otp(email, otp_value):
    message = get_new_otp_message(otp_value)
    print(type(message))
    return send_email(email, message)
