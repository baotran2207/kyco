from chalice import BadRequestError, Blueprint
from chalicelib.config import settings
from chalicelib.db.session import SessionLocal
from chalicelib.logger_app import logger
from chalicelib.services.github_service import update_file

unname_bp = Blueprint(__name__)


@unname_bp.route("/test_sqs", methods=["GET"])
def test_sqs():
    from chalicelib.services.sqs_service import send_message, sqs_generic

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
    query = db.execute("SELECT 1")
    logger.info(f" Connection ok ! Detail {query} ")
    logger.error(f"Connection ok ! ")
    print(logger.level)
    return "Connection is ok"


@unname_bp.route("/test_github")
def commit_github():
    filename = "autocommit.txt"
    repo = "baotran2207/til"
    return update_file(filename, "auto commit", repo)
