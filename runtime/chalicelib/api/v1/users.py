from chalice import Blueprint, Chalice
from chalicelib.dynamo_db.base import dynamodb_table
from chalicelib.logger_app import logger
from chalicelib.services.authorizers import chalice_authorizer, get_current_user

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


@users_blueprints.route("/user_info", methods=["GET"], authorizer=chalice_authorizer)
def user_info():
    headers = users_blueprints.current_app.current_request.headers
    current_user = get_current_user(users_blueprints.current_app.current_request)
    return current_user.dict()


@users_blueprints.route(
    "/users", methods=["GET", "POST"], authorizer=chalice_authorizer
)
def routes_users():
    route_method = users_blueprints.current_app.current_request.method


@users_blueprints.route(
    "/users/{user_id}", methods=["GET", "PUT", "DELETE"], authorizer=chalice_authorizer
)
def routes_user():
    route_method = users_blueprints.current_app.current_request.method
    user_id = users_blueprints.current_request.path_parameters["user_id"]
    logger.info(user_id)
