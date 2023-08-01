from chalice import BadRequestError, Blueprint
from chalicelib.config import settings
from chalicelib.controller.auth import (
    change_password,
    confirm_forgot_password,
    init_challenge,
    initiate_forgot_password,
    login,
    login_with_challenge,
    sign_up,
)
from chalicelib.logger_app import logger
from chalicelib.schemas import (
    UserAuth,
    UserChangePassword,
    UserConfirmForgotPassword,
    UserCreate,
    UserSignIn,
    UserSignInChallenge,
)
from chalicelib.services.authorizers import (
    authenticator,
    chalice_authorizer,
    get_current_user,
)
from chalicelib.utils import generate_new_password
from pydantic import ValidationError

# from chalicelib.services.users import create_user, get_user, login_user


auth_routes = Blueprint(__name__)


@auth_routes.route("/login", methods=["POST"])
def auth_login():
    params = auth_routes.current_app.current_request.json_body
    logger.debug(params)
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

    authenticator.confirm_user_sign_up(username=user.username, confirmation_code=confirmation_code)

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


@auth_routes.route("/change-password", methods=["POST"], authorizer=chalice_authorizer)
def route_change_password():
    params = auth_routes.current_app.current_request.json_body
    logger.debug(params)
    if not params:
        raise BadRequestError(f"missing required information : phone number OR email")
    try:
        user = UserChangePassword(**params)
    except ValidationError as e:
        raise BadRequestError(f"{e}")

    verify_code = change_password(user)

    logger.debug(user)

    return {"message": "password changed succeccfully ! You can login "}


@auth_routes.route("/forgot-password", methods=["POST"])
def forgot_password():
    params = auth_routes.current_app.current_request.json_body
    if not params:
        raise BadRequestError(f"missing required information : phone number OR email")
    try:
        user = UserAuth(**params)
    except ValidationError as e:
        raise BadRequestError(f"{e}")

    verify_code = initiate_forgot_password(user.username)
    return {"message": "A confirmation code sent to your email"}


@auth_routes.route("/confirm-forgot-password", methods=["POST"])
def route_confirm_forgot_password():
    params = auth_routes.current_app.current_request.json_body
    if not params:
        raise BadRequestError(f"missing required information : phone number OR email")
    try:
        logger.debug(params)
        user = UserForgotPassword(**params)
    except ValidationError as e:
        raise BadRequestError(f"{e}")

    response = confirm_forgot_password(user)

    logger.debug(response)

    return {"message": "password changed succeccfully ! You can login "}
