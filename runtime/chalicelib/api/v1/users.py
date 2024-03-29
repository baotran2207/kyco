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
    current_user = get_current_user(users_blueprints.current_app.current_request)
    logger.debug(current_user)

    return current_user.dict()


@users_blueprints.route(
    "/users", methods=["GET", "POST"], authorizer=chalice_authorizer
)
def routes_users():
    route_method = users_blueprints.current_app.current_request.method


@users_blueprints.route(
    "/users/{_id}",
    methods=["GET", "PUT", "PATCH", "DELETE"],
    authorizer=chalice_authorizer,
)
def routes_user(_id):
    route_method = users_blueprints.current_app.current_request.method
    current_user = get_current_user(users_blueprints.current_app.current_request)

    is_me = current_user.sub == _id

    return {"message": "ok"}
