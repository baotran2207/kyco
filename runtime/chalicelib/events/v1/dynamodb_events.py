# from chalice import Blueprint, Chalice
# from chalicelib.config import settings


# from chalicelib.blueprint import dynamodb_bp

# @dynamodb_bp.current_app.on_dynamodb_record(stream_arn=settings.DYNAMODB_STREAM_ARN)
# def handle_ddb_message(event):
#     for record in event:
#         dynamodb_bp.current_app.log.debug("New: %s", record.new_image)
