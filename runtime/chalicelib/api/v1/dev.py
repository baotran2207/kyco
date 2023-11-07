from chalice import BadRequestError, Blueprint
from chalicelib.config import settings
from chalicelib.db.session import SessionLocal
from chalicelib.events.base import add_filters_to_lambda_subscribers, post_event
from chalicelib.events.event_type import EventType
from chalicelib.logger_app import logger
from chalicelib.services.github_service import update_file
from chalicelib.services.sqs_service import send_message
from sqlalchemy.sql import text

# from chalicelib.services.porfolio import summary_sheet

unname_bp = Blueprint(__name__)


@unname_bp.route("/test_sqs", methods=["GET"])
def test_sqs():
    sqs_generic = get_queue(
        settings.SQS_GENERIC
        if "arn:aws:sqs" not in settings.SQS_GENERIC
        else settings.SQS_GENERIC.split(":")[-1]
    )
    logger.info("test message ")
    test = send_message(
        queue=sqs_generic,
        message_body="test sqs mesg",
        message_attributes={
            "path": {"StringValue": "test", "DataType": "String"},
            "line": {"StringValue": "trigger", "DataType": "String"},
        },
    )

    return test


@unname_bp.route("/check_db_connection")
def check_db_connection():
    db = SessionLocal()
    query = db.execute(text("SELECT 1"))
    logger.info(f" Connection ok ! Detail {query} ")
    return "Connection is ok"


@unname_bp.route("/test_github")
def commit_github():
    filename = "autocommit.txt"
    repo = "baotran2207/til"
    return update_file(filename, "auto commit", repo)


@unname_bp.route("/test_post_deploy_update_sns_subscribers")
def post_deploy_update_sns_subscribers():
    add_filters_to_lambda_subscribers()
    return {"message": "ok"}


@unname_bp.route("/test_event")
def post_deploy_update_sns_subscribers():
    post_event(EventType.POST_USER_REGISTER, {"username": "baotran2207"})
    return {"message": "ok"}


"""
https://nominatim.openstreetmap.org/search?q=%C4%90%C6%B0%E1%BB%9Dng%20Nguy%E1%BB%85n%20V%C4%83n%20Linh,%20Ph%C6%B0%E1%BB%9Dng%20T%C3%A2n%20Thu%E1%BA%ADn%20T%C3%A2y,%20Qu%E1%BA%ADn%207,%20Tp%20H%E1%BB%93%20Ch%C3%AD%20Minh&format=json&polygon=1&addressdetails=1
"""
