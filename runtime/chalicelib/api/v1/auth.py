from chalice import BadRequestError, Blueprint
from chalicelib.config import settings
from chalicelib.controller.auth import (
    init_challenge,
    login,
    login_with_challenge,
    sign_up,
)
from chalicelib.logger_app import logger
from chalicelib.schemas import UserAuth, UserCreate, UserSignIn, UserSignInChallenge
from chalicelib.services.authorizers import authenticator
from chalicelib.utils import generate_new_password
from pydantic import ValidationError

# from chalicelib.services.users import create_user, get_user, login_user


auth_routes = Blueprint(__name__)


@auth_routes.route("/login", methods=["POST"])
def auth_login():
    params = auth_routes.current_app.current_request.json_body
    user = UserSignIn(**params)
    reponse = login(user, authenticator)
    return reponse


@auth_routes.route("/init_challenge", methods=["GET", "POST"])
def route_init_challenge():
    params = auth_routes.current_app.current_request.json_body
    try:
        user = UserAuth(**params)
    except ValidationError as e:
        raise BadRequestError(f"{e}")

    challenge_session_id = init_challenge(username=user.username)
    return {
        "message": f"A otp sent to {user.username}",
        "challenge_session_id": challenge_session_id,
    }


@auth_routes.route("/login_with_challenge", methods=["POST"])
def route_login_with_challenge():
    params = auth_routes.current_app.current_request.json_body
    try:
        user_with_challenge = UserSignInChallenge(**params)
    except ValidationError as e:
        raise BadRequestError(f"{e}")

    reponse = login_with_challenge(
        username=user_with_challenge.username,
        challenge_session_id=user_with_challenge.challenge_session_id,
        challenge_answer=user_with_challenge.challenge_answer,
    )

    return reponse


@auth_routes.route("/resend_confirmation", methods=["POST"])
def resend_confirmation():
    params = auth_routes.current_app.current_request.json_body
    user = UserAuth(**params)
    delivery = authenticator.resend_confirmation(username=user.username)

    return delivery


@auth_routes.route("/verify_email", methods=["POST"])
def confirm_user():
    params = auth_routes.current_app.current_request.json_body
    try:
        user = UserAuth(**params)
    except ValidationError as e:
        raise BadRequestError(f"{e}")
    confirmation_code = params.get("confirmation_code")

    if not confirmation_code:
        raise BadRequestError("confirmation_code is required")

    authenticator.confirm_user_sign_up(
        username=user.username, confirmation_code=confirmation_code
    )

    return {"message": "Confirmed registration succeccfully ! You can login "}


@auth_routes.route("/register", methods=["POST", "GET"])
def register():
    params = auth_routes.current_app.current_request.json_body
    try:
        new_user_info = UserCreate(
            email=params.get("email"),
            phone_number=params.get("phone_number"),
            password=params.get("password") or generate_new_password(),
        )
    except ValidationError as e:
        raise BadRequestError(f"{e}")

    created_new_user = sign_up(new_user_info)
    return created_new_user.dict()
