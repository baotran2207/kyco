import requests
from app import app
from chalice.test import Client


def test_authorizer(headers_with_token, base_url):
    res = requests.get(
        url=f"{base_url}/user-pools",
        headers=headers_with_token,
    )
    assert res.status_code == 200


# def test_user_info(headers_with_token, base_url):
#     res = requests.get(
#         url=f"{base_url}/user_info",
#         headers=headers_with_token,
#     )
#     print(res.content)
#     assert res.status_code == 200


def test_init_route():
    with Client(app) as client:
        response = client.http.get("/")

        assert response.json_body == {
            "message": "Hello there from tranthanhbao2207@gmail.com"
        }
