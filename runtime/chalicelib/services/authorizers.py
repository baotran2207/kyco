from dataclasses import dataclass
from pprint import pprint
from typing import Protocol

import boto3
from chalice import CognitoUserPoolAuthorizer

from chalicelib.config import settings
from chalicelib.schemas import UserBase, UserCreate, UserLoginResponse, UserSignIn

cognito_authorizer = CognitoUserPoolAuthorizer(
    "BaoTranChaliceUserPool",
    header="Bearer",
    provider_arns=[settings.COGNITO_USER_POOL]
)


chalice_authorizer = cognito_authorizer
cognito_client = boto3.client("cognito-idp")


class Authorizer(Protocol):
    def sign_up(self, user: UserCreate):
        pass

    def confirm_sign_up(self, user: UserCreate):
        pass

    def sign_in(self, user: UserSignIn) -> UserLoginResponse:
        pass


@dataclass
class CognitoAuth:
    cognito_client: boto3.Session
    user_pool_id: str
    app_client_id: str

    def sign_up(self, user: UserCreate, is_auto_confirm=True):
        sign_up_response = self.cognito_client.sign_up(
            ClientId=self.app_client_id,
            Username=user.email,
            Password=user.password,
            UserAttributes=[{"Name": "email", "Value": user.email}],
        )
        pprint(sign_up_response)
        if is_auto_confirm:
            confirm_sign_up_response = self.confirm_sign_up(user)
            pprint(confirm_sign_up_response)

            user = UserBase(
                uuid=sign_up_response["UserSub"],
                meta_data={
                    "UserConfirmed": True,
                },
            )

            return user

        user = UserBase(
            uuid=sign_up_response["UserSub"],
            meta_data={
                "CodeDeliveryDetails": sign_up_response.get("CodeDeliveryDetails"),
                "UserConfirmed": sign_up_response.get("UserConfirmed"),
            },
        )
        return user

    def confirm_sign_up(self, user: UserCreate):
        confirm_sign_up_response = cognito_client.admin_confirm_sign_up(
            UserPoolId=self.user_pool_id, Username=user.email
        )
        return confirm_sign_up_response

    def sign_in(self, user: UserSignIn):
        response = cognito_client.initiate_auth(
            ClientId=self.app_client_id,
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={"USERNAME": user.email, "PASSWORD": user.password},
        )

        res = response["AuthenticationResult"]
        return UserLoginResponse(**res)


cognito_auth = CognitoAuth(
    cognito_client,
    settings.COGNITO_USER_POOL_ID,
    settings.COGNITO_APP_CLIENT_ID,
)
