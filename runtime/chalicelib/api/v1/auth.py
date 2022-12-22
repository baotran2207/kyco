from pprint import pprint

from chalice import BadRequestError, Blueprint
from chalicelib.config import settings
from chalicelib.schemas import UserCreate, UserSignIn
from chalicelib.services.authorizers import authenticator
from chalicelib.services.users import create_user, get_user, login_user
from pydantic import ValidationError

auth_routes = Blueprint(__name__)


@auth_routes.route("/register", methods=["POST", "GET"])
def login():
    params = auth_routes.current_app.current_request.json_body
    try:
        new_user_info = UserCreate(**params)
    except ValidationError as e:
        raise BadRequestError(f"{e}")

    created_new_user = create_user(new_user_info, authenticator)

    return created_new_user.dict()


@auth_routes.route("/login", methods=["POST"])
def lookup_user():
    params = auth_routes.current_app.current_request.json_body

    logging_user = UserSignIn(**params)

    reponse = login_user(logging_user, authenticator)
    return reponse.dict()


@auth_routes.route("/resend_confirmation", methods=["POST"])
def resend_confirmation():
    params = auth_routes.current_app.current_request.json_body
    email = params.get("email")
    if not email:
        raise BadRequestError("Username is required")
    delivery = authenticator.resend_confirmation(username=email)

    return delivery


@auth_routes.route("/confirm_user", methods=["POST"])
def confirm_user():
    params = auth_routes.current_app.current_request.json_body
    email = username = params.get("email")
    confirmation_code = params.get("confirmation_code")
    print(username)
    if not email:
        raise BadRequestError("Username is required")
    if not confirmation_code:
        raise BadRequestError("confirmation_code is required")

    authenticator.confirm_user_sign_up(
        username=username, confirmation_code=confirmation_code
    )

    return f"User {email} is confirmed , you can login now"
