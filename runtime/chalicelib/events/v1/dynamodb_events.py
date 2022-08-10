

from chalice import Blueprint, Chalice
from chalicelib.config import settings
dynamodb_bp = Blueprint(__name__)

@dynamodb_bp.on_dynamodb_record(stream_arn=settings.DYNAMODB_STREAM_ARN)
def handle_ddb_message(event):
    for record in event:
        dynamodb_bp.log.debug("New: %s", record.new_image)