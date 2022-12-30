from chalicelib.events import EventType, post_event
from chalicelib.schemas import UserSignIn
from chalicelib.services.authorizers import Authenticator
from chalicelib.services.authorizers import authenticator as cog_authenticator


def login(user: UserSignIn, authenticator: Authenticator = cog_authenticator):
    response = authenticator.sign_in(user)
    post_event(EventType.POST_USER_LOGIN, user)
    return response


# @users_blueprints.route("/users", methods=["POST"])
# def register_new_user(name: str, password: str, email: str):
#     # create an entry in the database
#     user = create_user(name, password, email)

#     # post an event
#     post_event("user_registered", user)

# @users_blueprints.route("/users", methods=["POST"])
# def password_forgotten(email: str):
#     # retrieve the user
#     user = find_user(email)

#     # generate a password reset code
#     user.reset_code = get_random_string(16)

#     # post an event
#     post_event("user_password_forgotten", user)

# def reset_password(code: str, email: str, password: str):

#     # retrieve the user
#     user = find_user(email)

#     # reset the password
#     user.reset_password(code, password)
