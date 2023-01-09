from aws_cdk import core as cdk


class CognitoAuth(cdk.Stack):
    """
    Init cognito and export to chalcie app
    """

    def __init__(self, scope, id, env_vars, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.env_vars = env_vars

    # self.cognito_app_client = self.user_pool.add_client(
    #     id=f"{self.PREFIX_ID}-app-client",
    #     user_pool_client_name=f"{self.PREFIX_NAME}ClientAuth",
    #     auth_flows=cognito.AuthFlow(user_password=True),
    #     generate_secret=False,
    # )
    # def _get_cognito(self, cognito_arn):
    #     user_pool =  cognito.UserPool(
    #         self,
    #         f"{self.PREFIX_ID}-users",
    #         user_pool_name=f"{self.PREFIX_NAME}Users",
    #         self_sign_up_enabled=True,
    #         sign_in_aliases=cognito.SignInAliases(
    #             email=True,
    #             phone=True,
    #         ),
    #         account_recovery=cognito.AccountRecovery.EMAIL_AND_PHONE_WITHOUT_MFA,
    #         # user_verification=cognito.UserVerificationConfig(
    #         #     email_subject="Verify your email for our awesome app!",
    #         #     email_body="Thanks for signing up to our awesome app! Your verification code is {####}",
    #         #     email_style=cognito.VerificationEmailStyle.CODE,
    #         #     sms_message="Thanks for signing up to our awesome app! Your verification code is {####}"
    #         # )
    #         standard_attributes=cognito.StandardAttributes(
    #             email=cognito.StandardAttribute(required=True, mutable=False),
    #             # phone=cognito.StandardAttribute(
    #             #     required=False,
    #             #     mutable=True
    #             # )
    #         ),
    #     )

    #     cdk.CfnOutput(self, f"{self.PREFIX_ID}-users-pool-name", value=user_pool.user_pool_provider_name)
    #     cdk.CfnOutput(self, f"{self.PREFIX_ID}-users-pool-arn", value=user_pool.user_pool_arn)
    #     return user_pool

    pass
