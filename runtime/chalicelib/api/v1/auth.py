
from chalice import Blueprint
from chalicelib.schemas import UserCreate, UserSignIn
from chalicelib.config import settings

from chalicelib.services.authorizers import cognito_auth
from chalicelib.services.users import create_user, login_user, get_user
from pprint import pprint


auth_routes = Blueprint(__name__)

@auth_routes.route('/register', methods=['POST', "GET"])
def login():
    params = auth_routes.current_app.current_request.json_body

    new_user_info = UserCreate(**params)

    created_new_user = create_user(new_user_info, cognito_auth)

    pprint(created_new_user)
    return created_new_user.dict()


@auth_routes.route('/login', methods=['POST'])
def lookup_user():
    params = auth_routes.current_app.current_request.json_body

    logging_user = UserSignIn(
       **params
    )

    reponse = login_user(logging_user, cognito_auth)
    return reponse.dict()
