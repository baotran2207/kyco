from urllib import response
from chalicelib.schemas import UserCreate, UserSignIn
from chalicelib.services.authorizers import Authorizer



def create_user(user: UserCreate , authorizer: Authorizer):
    created_user = authorizer.sign_up(user)
    return created_user


def get_user(user: UserSignIn, authorizer: Authorizer):
    pass

def login_user(user: UserSignIn, authorizer: Authorizer):
    response = authorizer.sign_in(user)
    return response