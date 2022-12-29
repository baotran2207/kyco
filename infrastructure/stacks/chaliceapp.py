import os
from unicodedata import name

import aws_cdk.aws_ssm as ssm
from aws_cdk import Duration
from aws_cdk import aws_cognito as cognito
from aws_cdk import (
    aws_dynamodb as dynamodb,  # aws_sns,; aws_cloudwatch as aws_cw,; aws_iam as iam_,
)
from aws_cdk import aws_s3
from aws_cdk import aws_s3_notifications as aws_s3_noti
from aws_cdk import aws_sqs

try:
    from aws_cdk import core as cdk
except ImportError:
    import aws_cdk as cdk

from chalice.cdk import Chalice

RUNTIME_SOURCE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), os.pardir, "runtime"
)


class ChaliceApp(cdk.Stack):
    def __init__(self, scope, id, env_vars, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.env_vars = env_vars
        self.PREFIX_NAME = self.env_vars.get("PROJECT_NAME").capitalize()
        self.PREFIX_ID = f"{self.PREFIX_NAME}-id".lower()

        self.dynamodb_table = self._create_ddb_table()
        # self.parameter_store_config = self._create_ssm()
        self.bucket = self._create_s3_bucket()
        self.sqs_sendemail = self._create_sqs("send-email", "SendEmail")
        self.sqs_generic = self._create_sqs(
            "generic-queue", "Generic"
        )  # for generic task
        # self.sqs_dead_letter = self._create_sqs("deadletter-queue", "DeadLetter") # for
        self.sqs_dead_letter = aws_sqs.DeadLetterQueue(
            max_receive_count=123,
            queue=self.sqs_generic,
        )

        self.imported_user_pool = cognito.UserPool.from_user_pool_arn(
            self,
            id=f"{self.PREFIX_ID}-pre-config-user-pool",
            user_pool_arn=self.env_vars.get("COGNITO_USER_POOL_ARN"),
        )

        # self.user_pool = self._create_cognito()
        # self.cognito_app_client = self.user_pool.add_client(
        #     id=f"{self.PREFIX_ID}-app-client",
        #     user_pool_client_name=f"{self.PREFIX_NAME}ClientAuth",
        #     auth_flows=cognito.AuthFlow(user_password=True),
        #     generate_secret=False,
        # )

        self.chalice = Chalice(
            self,
            "BaoTranBackend",
            source_dir=RUNTIME_SOURCE_DIR,
            stage_config={
                "lambda_memory_size": 256,
                "environment_variables": {
                    "APP_TABLE_NAME": self.dynamodb_table.table_name,
                    "ENV": "prod",
                    "S3_MAIN_BUCKET": self.bucket.bucket_name,
                    "SQS_GENERIC": self.sqs_generic.queue_arn,
                    "SQS_SENDEMAIL": self.sqs_sendemail.queue_arn,
                    "COGNITO_USER_POOL_NAME": "Load from env_vars which is .prod",
                    "COGNITO_USER_POOL_ARN": "Load from env_vars which is .prod",
                    "COGNITO_APP_CLIENT_ID": "Load from env_vars which is .prod",
                    # "DYNAMODB_STREAM_ARN": DYNAMODB_STREAM_ARN,  # TODO: get DYNAMODB_STREAM_ARN from table
                }
                | self.env_vars,
            },
        )

        self.chalice_role = self.chalice.get_role("DefaultRole")

        self.bucket.grant_read_write(self.chalice_role)
        self.bucket.add_event_notification(
            aws_s3.EventType.OBJECT_CREATED_PUT,
            aws_s3_noti.SqsDestination(self.sqs_generic),
        )
        self.dynamodb_table.grant_read_write_data(self.chalice.get_role("DefaultRole"))
        # self.parameter_store_config.grant_read(self.chalice.get_role("DefaultRole"))

        self.sqs_sendemail.grant_consume_messages(self.chalice.get_role("DefaultRole"))
        self.sqs_sendemail.grant_send_messages(self.chalice.get_role("DefaultRole"))
        self.sqs_generic.grant_consume_messages(self.chalice.get_role("DefaultRole"))
        self.sqs_generic.grant_send_messages(self.chalice.get_role("DefaultRole"))

        self.imported_user_pool.grant(
            self.chalice.get_role("DefaultRole"), "cognito-idp:AdminCreateUser"
        )

    def _create_s3_bucket(self):
        return aws_s3.Bucket(
            self,
            id=f"{self.PREFIX_ID}-mainbucket-",
            # bucket_name=f"{PREFIX_NAME.lower()}-main",
        )

    def _create_ddb_table(self):
        dynamodb_table = dynamodb.Table(
            self,
            f"{self.PREFIX_ID}-table",
            partition_key=dynamodb.Attribute(
                name="PK", type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(name="SK", type=dynamodb.AttributeType.STRING),
            stream=dynamodb.StreamViewType.NEW_IMAGE,
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )
        cdk.CfnOutput(
            self, f"{self.PREFIX_ID}-table-name", value=dynamodb_table.table_name
        )
        return dynamodb_table

    def _create_sqs(self, id: str, sqs_name: str) -> aws_sqs.Queue:
        # Function timeout <= SQS timeout . Currently function timeout is 60s, TODO: reduce both function timeout and queue timeout
        return aws_sqs.Queue(
            self,
            f"{self.PREFIX_ID}-{id}",
            queue_name=f"{self.PREFIX_NAME}{sqs_name.capitalize()}",
            visibility_timeout=Duration.seconds(60),
        )

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
