import pytest
from chalicelib.config import settings
from chalicelib.controller.auth import login
from chalicelib.schemas import UserSignIn


@pytest.fixture(scope="session")
def token_id():
    username = settings.WEBMASTER_EMAIL
    password = settings.WEBMASTER_PASSWORD
    user = UserSignIn(email=username, password=password)
    response = login(user)
    token_id = response.get("IdToken")
    return token_id


@pytest.fixture(scope="session")
def headers_with_token(token_id):
    return {"Bearer": f"{token_id}"}


@pytest.fixture(scope="session")
def base_url():
    return "https://zr0fxh86b0.execute-api.ap-southeast-1.amazonaws.com/api"
