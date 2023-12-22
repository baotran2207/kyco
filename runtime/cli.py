import json

import chalicelib.schemas.messages as messages
import chalicelib.services.ses_service as ses_service
import typer

app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


@app.command()
def send_templated_email():
    email_message = messages.EmailSqsMessage(
        to_emails=["tranthanhbao2207@gmail.com"],
        template_name="KycoNEW_OTP",
        email_payload={"otp_code": "123456"},
        source="tranthanhbao2207@gmail.com",
    )

    ses_service.ses_mail_sender.send_templated_email(
        to_emails=email_message.to_emails,
        template_name=email_message.template_name,
        template_data=email_message.email_payload,
        source=email_message.source,
        cc_emails=email_message.cc_emails,
        bcc_emails=email_message.bcc_emails,
        reply_tos=email_message.reply_tos,
    )


@app.command()
def mdm():
    from chalicelib.modeler import mdm

    mdm.main()


def main():
    app()


if __name__ == "__main__":
    app()
