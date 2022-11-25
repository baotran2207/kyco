import os
import queue
from unicodedata import name
import json
from aws_cdk import (
    aws_dynamodb as dynamodb,
    aws_s3,
    aws_sns,
    aws_sqs,
    aws_cloudwatch as aws_cw,
    aws_iam as iam_,
    aws_cognito as cognito,
    aws_s3_notifications as aws_s3_noti,
    Duration
)

try:
    from aws_cdk import core as cdk
except ImportError:
    import aws_cdk as cdk

from chalice.cdk import Chalice


RUNTIME_SOURCE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), os.pardir, "runtime"
)



CURDIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))

SECRET_FILE_PATH = os.path.join(
    CURDIR,"assets", "ssm_parameter_store", "prod.json"
)

PREFIX_NAME = "BaoTranChalice" # Example: DataLakeCdkBlog
PREFIX_ID = "baotran-chalice-id" # Example: unique-identifier-data-lake

PRE_CREATED_PARAMETER_STORE_NAME = "/chalice_backend/prod"

def get_config_secret(file_path: os.path) -> dict:
    f = open(file_path)
    ssm_config = json.load(f)
    return ssm_config

ssm_config = get_config_secret(SECRET_FILE_PATH)

import aws_cdk.aws_ssm as ssm
class ChaliceApp(cdk.Stack):
    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)
        self.dynamodb_table = self._create_ddb_table()
        self.parameter_store_config = self._create_ssm()
        self.bucket = self._create_s3_bucket()
        self.sqs_sendemail = self._create_sqs("send-email", "SendEmail")
        self.sqs_generic = self._create_sqs("generic-queue", "Generic") # for generic task
        # self.sqs_dead_letter = self._create_sqs("deadletter-queue", "DeadLetter") # for
        self.sqs_dead_letter = aws_sqs.DeadLetterQueue(
            max_receive_count=123,
            queue=self.sqs_generic,
        )

        self.user_pool = self._create_cognito()
        self.cognito_app_client = self.user_pool.add_client(
            id=f"{PREFIX_ID}-app-client",
            user_pool_client_name=f"{PREFIX_NAME}ClientAuth",
            auth_flows=cognito.AuthFlow(user_password=True),
            generate_secret=False,
        )


        self.chalice = Chalice(
            self,
            "BaoTranBackend",
            source_dir=RUNTIME_SOURCE_DIR,
            stage_config={
                "lambda_memory_size": 256,
                "environment_variables": {
                    "APP_TABLE_NAME": self.dynamodb_table.table_name,
                    "ENV": "prod",
                    "SSM_NAME": PRE_CREATED_PARAMETER_STORE_NAME,

                    "S3_MAIN_BUCKET": self.bucket.bucket_name,
                    "SQS_GENERIC" : self.sqs_generic.queue_name,
                    "SQS_SENDEMAIL" : self.sqs_sendemail.queue_name,
                    # "SQS_DEADLETTER" : self.sqs_dead_letter.queue_name,

                    "COGNITO_USER_POOL": self.user_pool.user_pool_arn,
                    "COGNITO_APP_CLIENT_ID": self.cognito_app_client.user_pool_client_id,
                    # "DYNAMODB_STREAM_ARN": DYNAMODB_STREAM_ARN,  # TODO: get DYNAMODB_STREAM_ARN from table
                }
            },
        )

        self.chalice_role = self.chalice.get_role("DefaultRole")

        self.bucket.grant_read_write(self.chalice_role)
        self.bucket.add_event_notification(aws_s3.EventType.OBJECT_CREATED_PUT, aws_s3_noti.SqsDestination(self.sqs_generic))
        self.dynamodb_table.grant_read_write_data(self.chalice.get_role("DefaultRole"))
        self.parameter_store_config.grant_read(self.chalice.get_role("DefaultRole"))

        self.sqs_sendemail.grant_consume_messages(self.chalice.get_role("DefaultRole"))
        self.sqs_sendemail.grant_send_messages(self.chalice.get_role("DefaultRole"))
        self.sqs_generic.grant_consume_messages(self.chalice.get_role("DefaultRole"))
        self.sqs_generic.grant_send_messages(self.chalice.get_role("DefaultRole"))

        self.user_pool.grant(self.chalice.get_role("DefaultRole"), "cognito-idp:AdminCreateUser")


    def _create_s3_bucket(self):
        return aws_s3.Bucket(self,
            id=f"{PREFIX_ID}-main",
            # bucket_name=f"{PREFIX_NAME.lower()}-main",
        )

    def _create_ddb_table(self):
        dynamodb_table = dynamodb.Table(
            self,
            f"{PREFIX_ID}-table",
            partition_key=dynamodb.Attribute(
                name="PK", type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(name="SK", type=dynamodb.AttributeType.STRING),
            stream=dynamodb.StreamViewType.NEW_IMAGE,
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )
        cdk.CfnOutput(self, "AppTableName", value=dynamodb_table.table_name)
        return dynamodb_table

    def _create_ssm(self):
        ps_object = ssm.StringParameter.from_string_parameter_name(self, f"{PREFIX_ID}-precreated", string_parameter_name=PRE_CREATED_PARAMETER_STORE_NAME)
        return ps_object

    def _create_sqs(self,id:str, sqs_name: str) -> aws_sqs.Queue:
        return aws_sqs.Queue(self,
            f"{PREFIX_ID}-{id}",
            queue_name=f"{PREFIX_NAME}{sqs_name.capitalize()}",
            visibility_timeout=Duration.seconds(60), ## Function timeout <= SQS timeout . Currently function timeout is 60s, TODO: reduce both function timeout and queue timeout

        )

    def _create_cognito(self):
        return cognito.UserPool(
            self,
            f"{PREFIX_ID}-users-pool",
            user_pool_name=f"{PREFIX_NAME}UsersPool",
            self_sign_up_enabled=True,
            sign_in_aliases=cognito.SignInAliases(
                email=True,
                phone=True,
            ),
            account_recovery=cognito.AccountRecovery.EMAIL_AND_PHONE_WITHOUT_MFA,
            # user_verification=cognito.UserVerificationConfig(
            #     email_subject="Verify your email for our awesome app!",
            #     email_body="Thanks for signing up to our awesome app! Your verification code is {####}",
            #     email_style=cognito.VerificationEmailStyle.CODE,
            #     sms_message="Thanks for signing up to our awesome app! Your verification code is {####}"
            # )
            standard_attributes=cognito.StandardAttributes(
                email=cognito.StandardAttribute(
                    required=True,
                    mutable=False
                ),
                # phone=cognito.StandardAttribute(
                #     required=False,
                #     mutable=True
                # )
            ),

        )

