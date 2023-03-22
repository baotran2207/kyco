import random
import json
from chalice import AuthResponse, Blueprint, Chalice
from chalice.app import Cron, Rate
from chalicelib.blueprint import events_blueprints, init_blueprint
from chalicelib.config import settings
from chalicelib.events.base import init_listeners
from chalicelib.logger_app import logger
from chalicelib.middlewares import init_middlewares
from chalicelib.services.authorizers import chalice_authorizer
from chalicelib.services.github_service import update_file

app = Chalice(app_name=settings.PROJECT_NAME, configure_logs=False)
app.api.cors = True


def create_app():
    # not supported yet : https://github.com/aws/chalice/issues/1587
    pass


@app.route("/user-pools", methods=["GET"], authorizer=chalice_authorizer)
def authenticated():
    return {"message": "authorized"}


@app.route("/")
def health():
    logger.info("app is ready!")
    return {"message": "Hello there from tranthanhbao2207@gmail.com"}


init_listeners()
init_blueprint(app)
# init_middlewares(app)

############
## Events ##
############
# ref:
#     - https://github.com/aws/chalice/issues/1566
# Due to bug in blueprint register , we can only register API endpoint,
# Workaround:
# - Register in app.py
# - lazy register in end of app.py


s3_events = Blueprint(__name__)


# TODO: https://aws.github.io/chalice/topics/events.html#s3-events current version does not support existing bucket created via cdk .
@s3_events.on_s3_event(
    bucket=settings.S3_MAIN_BUCKET, prefix="users_upload", events=["s3:ObjectCreated:*"]
)
def handle_s3_event(event):
    logger.info("Received event for bucket: %s, key: %s", event.bucket, event.key)


# app.register_blueprint(s3_events)

for event_bp in events_blueprints:
    app.register_blueprint(event_bp)
