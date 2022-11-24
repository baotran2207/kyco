

from chalice import Blueprint, Chalice

from chalicelib.dynamo_db.base import dynamodb_table
from chalicelib.services.users import get_user
from chalicelib.services.authorizers import chalice_authorizer
users_blueprints = Blueprint(__name__)


# @users_blueprints.route('/users', methods=['POST'])
# def create_user():
#     request = users_blueprints.current_app.current_request.json_body
#     item = {
#         'PK': 'User#%s' % request['username'],
#         'SK': 'Profile#%s' % request['username'],
#     }
#     item.update(request)
#     dynamodb_table.put_item(Item=item)
#     return item


@users_blueprints.route('/user_info', methods=['GET'], authorizer=chalice_authorizer)
def user_info():
    headers = users_blueprints.current_app.current_request.headers
    print(headers)
    return 'ok'

@users_blueprints.route('/users', methods=['GET'])
def get_users():
    return "ok"
