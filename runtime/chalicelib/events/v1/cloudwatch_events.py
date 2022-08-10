

from chalice import Blueprint, Chalice


cw_bp = Blueprint(__name__)

# @cw_bp.on_cw_event({"source": ["aws.codecommit"]})
# def on_code_commit_changes(event):
#     print(event.to_dict())
