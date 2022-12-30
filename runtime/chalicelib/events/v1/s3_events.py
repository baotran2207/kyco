from chalice import Blueprint, Chalice
from chalicelib.config import settings
from chalicelib.logger_app import logger

s3_events = Blueprint(__name__)
# @s3_bp.on_s3_event(bucket='databricks-workspace-stack-lambdazipsbucket-1or12r81xzxfg',
#                  events=['s3:ObjectCreated:*'])
# def handle_s3_event(event):
#     s3_bp.current_app.log.debug("Received event for bucket: %s, key: %s",
#                   event.bucket, event.key)


@s3_events.on_s3_event(
    bucket=settings.S3_MAIN_BUCKET, prefix="users_upload", events=["s3:ObjectCreated:*"]
)
def handle_s3_event(event):
    logger.info("Received event for bucket: %s, key: %s", event.bucket, event.key)
