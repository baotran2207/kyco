# from chalice import Blueprint
# from chalicelib.config import settings
# # from chalicelib.blueprint import sqs_bp


# sqs_bp = Blueprint(__name__)
# @sqs_bp.current_app.on_sqs_message(
#     queue='BaoTranChaliceGeneric', batch_size=1)
# def handle_sqs_message(event):
#     print('Trigger generic')
#     for record in event:
#         sqs_bp.current_app.log.debug("Received message with contents: %s", record.body)
