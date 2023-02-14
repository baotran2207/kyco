import json
from dataclasses import dataclass
from typing import Protocol

import boto3
from botocore.exceptions import ClientError
from chalice import (
    BadRequestError,
    ChaliceUnhandledError,
    CognitoUserPoolAuthorizer,
    ConflictError,
    UnauthorizedError,
)
from chalicelib.config import settings
from chalicelib.logger_app import logger
from chalicelib.schemas import UserBase, UserCreate, UserLoginResponse, UserSignIn

cognito_authorizer = CognitoUserPoolAuthorizer(
    settings.COGNITO_USER_POOL_NAME,
    header="Bearer",
    provider_arns=[settings.COGNITO_USER_POOL_ARN],
)


chalice_authorizer = cognito_authorizer
cognito_client = boto3.client("cognito-idp")


class Authenticator(Protocol):
    def sign_up(self, user: UserCreate):
        pass

    def confirm_user_sign_up(self, user: UserCreate, confirmation_code: str):
        pass

    def confirm_user_admin_sign_up(self, user: UserCreate):
        pass

    def sign_in(self, username, password) -> UserLoginResponse:
        pass

    def _secret_hash(self, user_name) -> str:
        pass

    def get_mfa_secret(self):
        pass

    def verify_mfa(self):
        pass

    def respond_to_mfa_challenge(self):
        pass

    def confirm_mfa_device(self):
        pass

    def list_users(self):
        pass

    def initiate_auth(self):
        pass

    def reset_password(self, username):
        pass

    def forgot_password(self, username):
        pass


@dataclass
class CognitoAuthFlow:
    """
    'SMS_MFA'|'SOFTWARE_TOKEN_MFA'|'SELECT_MFA_TYPE'|
    'MFA_SETUP'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|
    'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|
    'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',

    """

    # Normal login : with username and password
    USER_PASSWORD_AUTH = "USER_PASSWORD_AUTH"
    # Custom auth lambda: define challenge + create auth + verify auth
    CUSTOM_CHALLENGE = "CUSTOM_CHALLENGE"


@dataclass
class CognitoAuth:
    cognito_client: boto3.Session
    user_pool_id: str
    app_client_id: str

    def list_users(self):
        try:
            response = self.cognito_client.list_users(UserPoolId=self.user_pool_id)
            users = response.get("Users")
        except ClientError as err:
            err_code = err.response["Error"]["Code"]
            err_msg = err.response["Error"]["Message"]
            res_msg = f"Couldn't list users for . Here's why: {err_code}: {err_msg}"
            logger.error(res_msg)
            raise ChaliceUnhandledError(res_msg)
        else:
            return users

    def get_user(self, access_token: str):
        user = self.cognito_client.get_user(
            # ClientId=self.app_client_id,
            AccessToken=access_token,
        )
        return user

    def sign_up(self, user: UserCreate, is_auto_confirm=False):
        user_attr = [
            {"Name": "email", "Value": user.email or ""},
            {"Name": "phone_number", "Value": user.phone_number or ""},
        ]
        try:
            sign_up_response = self.cognito_client.sign_up(
                ClientId=self.app_client_id,
                Username=user.username,
                Password=user.password,
                UserAttributes=user_attr,
            )
        except cognito_client.exceptions.UsernameExistsException as e:
            raise ConflictError(f"{e}")

        user = UserBase(
            uuid=sign_up_response["UserSub"],
            meta_data={
                "CodeDeliveryDetails": sign_up_response.get("CodeDeliveryDetails"),
                "UserConfirmed": sign_up_response.get("UserConfirmed"),
            },
        )
        return user

    def confirm_user_admin_sign_up(self, user: UserCreate):
        confirm_sign_up_response = cognito_client.admin_confirm_sign_up(
            UserPoolId=self.user_pool_id, Username=user.email
        )
        return confirm_sign_up_response

    def resend_confirmation(self, username):
        try:
            response = self.cognito_client.resend_confirmation_code(
                ClientId=self.app_client_id, Username=username
            )
            logger.debug(response)
            delivery = response["CodeDeliveryDetails"]
        except ClientError as err:
            err_code = err.response["Error"]["Code"]
            err_msg = err.response["Error"]["Message"]
            res_msg = f"Couldn't resend confirmation to {username}. Here's why: {err_code}: {err_msg}"
            logger.error(res_msg)
            raise ChaliceUnhandledError(res_msg)

        else:
            return delivery

    def confirm_user_sign_up(self, username: str, confirmation_code):
        try:
            self.cognito_client.confirm_sign_up(
                ClientId=self.app_client_id,
                ConfirmationCode=str(confirmation_code),
                Username=username,
            )
        except ClientError as err:
            err_code = err.response["Error"]["Code"]
            err_msg = err.response["Error"]["Message"]
            res_msg = f"Couldn't confirm sign up for  {username}. Here's why: {err_code}: {err_msg}"
            logger.error(res_msg)
            raise ChaliceUnhandledError(res_msg)
        else:
            return True

    def sign_in(self, username: str, password: str):

        try:
            response = cognito_client.initiate_auth(
                ClientId=self.app_client_id,
                AuthFlow=CognitoAuthFlow.USER_PASSWORD_AUTH,
                AuthParameters={"USERNAME": username, "PASSWORD": password},
            )
            res = response["AuthenticationResult"]
        except ClientError as err:
            err_code = err.response["Error"]["Code"]
            err_msg = err.response["Error"]["Message"]
            logger.info(err.response["Error"])
            if err_code == "NotAuthorizedException":
                raise UnauthorizedError(err_msg)
            raise BadRequestError(err.response)

        return UserLoginResponse(**res).dict()

    def init_challenge(self, username):
        """
        this will send an challenge (eg: otp) to username (email | phone)
        depend on cognito_events
        """
        try:
            response = self.cognito_client.initiate_auth(
                AuthFlow="CUSTOM_AUTH",
                ClientId=self.app_client_id,
                AuthParameters={
                    "USERNAME": username,
                },
            )
            return response["Session"]

        except ClientError as err:
            err_code = err.response["Error"]["Code"]
            err_msg = err.response["Error"]["Message"]
            logger.exception(err.response["Error"])
            raise BadRequestError(err.response)

    def verify_challenge(self, username, challenge_session_id, challenge_answer):
        """
        depend on cognito_events
        """
        try:
            response = self.cognito_client.respond_to_auth_challenge(
                ChallengeName=CognitoAuthFlow.CUSTOM_CHALLENGE,
                ClientId=self.app_client_id,
                Session=challenge_session_id,
                ChallengeResponses={
                    "ANSWER": challenge_answer,
                    "USERNAME": username,
                },
            )

            if "AuthenticationResult" in response:
                return UserLoginResponse(**response["AuthenticationResult"]).dict()
            raise BadRequestError("challenge_answer is not correct")

        except ClientError as err:
            err_code = err.response["Error"]["Code"]
            err_msg = err.response["Error"]["Message"]
            logger.exception(err.response["Error"])
            raise BadRequestError(err.response)

        """respond_to_auth_challenge"""

    def reset_password(self, username):
        pass

    def forgot_password(self, username):
        pass


cog_authenticator = CognitoAuth(
    cognito_client,
    settings.COGNITO_USER_POOL_ID,
    settings.COGNITO_APP_CLIENT_ID,
)

authenticator = cog_authenticator
