# from chalice import Blueprint, Chalice

# cw_bp = Blueprint(__name__)
# # Cron(0, 10, '*', '*', '?', '*')
# # @cw_bp.on_cw_event({"source": ["aws.codecommit"]})
# # def on_code_commit_changes(event):
# #     print(event.to_dict())

# @cw_bp.schedule('rate(1 hour)')
# def every_hour(event):
#     print('test cron 1 hour')
#     print(event.to_dict())
