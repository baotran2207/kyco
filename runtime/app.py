import random

from chalicelib.logger_app import logger, init_logger
from chalice import AuthResponse, Blueprint, Chalice
from chalice.app import Cron, Rate
from chalicelib.blueprint import events_blueprints, init_blueprint
from chalicelib.config import settings
from chalicelib.db.session import SessionLocal
from chalicelib.events.base import init_listeners
from chalicelib.middlewares import init_middlewares
from chalicelib.services.authorizers import chalice_authorizer
from chalicelib.services.github_service import update_file

app = Chalice(app_name=settings.PROJECT_NAME)
print(app.log.name)
init_logger(app)
@app.route("/user-pools", methods=["GET"], authorizer=chalice_authorizer)
def authenticated():
    return {"success": True}


@app.route("/")
def health():
    return "Hello there from tranthanhbao2207@gmail.com"


init_listeners()
init_blueprint(app)
init_middlewares(app)

############
## Events ##
############
# ref:
#     - https://github.com/aws/chalice/issues/1566
# Due to bug in blueprint register , we can only register API endpoint, but events and pure function. Let keep those events and pure function here in app.py until the bug is fixed


cron_events = Blueprint(__name__)
# sqs_events = Blueprint(__name__)
s3_events = Blueprint(__name__)


@cron_events.schedule(Cron(0, 18, "?", "*", "*", "*"))
def warm_up_db_everyday(event):
    logger.info("Warm up Superbase database !")
    db = SessionLocal()
    a = db.execute("SELECT 1")
    return "This should be invoked every weekday at 6pm"


@cron_events.schedule(Rate(8, unit=Rate.HOURS))
def auto_commit_cron(event):
    if random.choice([True, False]):
        filename = "autocommit.txt"
        repo = "baotran2207/til"
        update_file(filename, "auto commit", repo)
    else:
        logger.info("No commit !")


# @sqs_events.on_sqs_message(queue_arn=settings.SQS_GENERIC, batch_size=1)
# def handle_sqs_generic(event):
#     logger.info("Trigger generic")
#     logger.info("dict ", event.to_dict())
#     logger.info("body ", event.body)
#     logger.info("body ", event.body)
#     for record in event:
#         logger.info(f" in even ! Detail {record} ")


# @sqs_events.on_sqs_message(queue_arn=settings.SQS_SENDEMAIL, batch_size=1)
# def handle_sqs_email(event):
#     logger.info("Trigger email")
#     logger.info("dict ", event.to_dict())
#     logger.info("body ", event.body)
#     logger.info("body ", event.body)
#     for record in event:
#         logger.info(f" in even ! Detail {record} ")


# TODO: https://aws.github.io/chalice/topics/events.html#s3-events current version does not support existing bucket created via cdk .
@s3_events.on_s3_event(
    bucket=settings.S3_MAIN_BUCKET, prefix="users_upload", events=["s3:ObjectCreated:*"]
)
def handle_s3_event(event):
    logger.info("Received event for bucket: %s, key: %s", event.bucket, event.key)


app.register_blueprint(cron_events)
# app.register_blueprint(sqs_events)
# app.register_blueprint(s3_events)

for event_bp in events_blueprints:
    app.register_blueprint(event_bp)
