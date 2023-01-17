from chalice import BadRequestError, Blueprint
from chalicelib.config import settings
from chalicelib.controller.auth import (
    init_challenge,
    login,
    login_with_challenge,
    sign_up,
)
from chalicelib.logger_app import logger
from chalicelib.schemas import UserCreate, UserSignIn
from chalicelib.services.authorizers import authenticator
from pydantic import ValidationError

# from chalicelib.services.users import create_user, get_user, login_user


auth_routes = Blueprint(__name__)


@auth_routes.route("/login", methods=["POST"])
def auth_login():
    params = auth_routes.current_app.current_request.json_body
    logging_user = UserSignIn(**params)
    reponse = login(logging_user, authenticator)
    return reponse


@auth_routes.route("/init_challenge", methods=["GET", "POST"])
def route_init_challenge():
    params = auth_routes.current_app.current_request.json_body
    phone = params.get("phone")
    email = params.get("email")

    user_to_lookup = UserSignIn(phone=phone, email=email)
    if email:
        challenge_session_id = init_challenge(username=user_to_lookup.username)
    logger.debug(challenge_session_id)
    return {
        "message": f"A otp sent to {email or phone}",
        "challenge_session_id": challenge_session_id,
    }


@auth_routes.route("/login_with_challenge", methods=["POST"])
def route_login_with_challenge():
    params = auth_routes.current_app.current_request.json_body
    phone = params.get("phone")
    email = params.get("email")
    username = phone or email
    challenge_answer = params.get("challenge_answer")
    challenge_session_id = params.get("challenge_session_id")

    reponse = login_with_challenge(
        username=username,
        challenge_session_id=challenge_session_id,
        challenge_answer=challenge_answer,
    )

    return reponse


@auth_routes.route("/resend_confirmation", methods=["POST"])
def resend_confirmation():
    params = auth_routes.current_app.current_request.json_body
    email = params.get("email")
    if not email:
        raise BadRequestError("Username is required")
    delivery = authenticator.resend_confirmation(username=email)

    return delivery


@auth_routes.route("/verify_email", methods=["POST"])
def confirm_user():
    params = auth_routes.current_app.current_request.json_body
    email = username = params.get("username") or params.get("email")
    confirmation_code = params.get("confirmation_code")

    if not email:
        raise BadRequestError("Username is required")
    if not confirmation_code:
        raise BadRequestError("confirmation_code is required")

    authenticator.confirm_user_sign_up(
        username=username, confirmation_code=confirmation_code
    )

    return f"User {email} is confirmed , you can login now"


@auth_routes.route("/register", methods=["POST", "GET"])
def register():
    params = auth_routes.current_app.current_request.json_body
    email = username = params.get("username") or params.get("email")
    try:
        new_user_info = UserCreate(**params)
    except ValidationError as e:
        raise BadRequestError(f"{e}")

    created_new_user = sign_up(new_user_info)
    return created_new_user.dict()


@auth_routes.route("/register_otp", methods=["POST", "GET"])
def register_otp():
    params = auth_routes.current_app.current_request.json_body
    logger.debug("not implment")
    return created_new_user.dict()
