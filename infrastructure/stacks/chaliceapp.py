import os
from unicodedata import name

import aws_cdk.aws_ssm as ssm
from aws_cdk import Duration
from aws_cdk import aws_cognito as cognito
from aws_cdk import (
    aws_dynamodb as dynamodb,  # aws_ses as ses,; aws_sns,;; aws_cloudwatch as aws_cw,;;
)
from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3
from aws_cdk import aws_s3_notifications as aws_s3_noti
from aws_cdk import aws_ses as ses
from aws_cdk import aws_sns, aws_sqs

try:
    from aws_cdk import core as cdk
except ImportError:
    import aws_cdk as cdk

from typing import Sequence

from chalice.cdk import Chalice

RUNTIME_SOURCE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), os.pardir, "runtime"
)
# }
from emails_templates_config import EmailTemplate, emails_templates
from loguru import logger

# logger.setLevel(logging.DEBUG)
# COGNITO_TRIGGER_HOOKS = {
#     "pre_sign_up": "PreSignUp",
#     "post_authentication": "PostAuthentication",
#     "pre_authentication": "PreAuthentication",


class ChaliceApp(cdk.Stack):
    def __init__(self, scope, id, env_vars, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.env_vars = env_vars
        self.ENV = self.env_vars.get("ENV")
        self.PREFIX_NAME = self.env_vars.get("PROJECT_NAME").capitalize()
        self.PREFIX_ID = f"{self.PREFIX_NAME}-id".lower()

        self.ses_emails_templates = [
            self._create_email_templates(email_template)
            for email_template in emails_templates
        ]
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
        self.sns_topic = aws_sns.Topic(
            self,
            id=f"{self.PREFIX_ID}-publisher",
            topic_name=f"{self.PREFIX_NAME}Publisher",
            display_name=f"{self.PREFIX_NAME}MainPublisher",
        )

        self.imported_user_pool = cognito.UserPool.from_user_pool_arn(
            self,
            id=f"{self.PREFIX_ID}-pre-config-user-pool",
            user_pool_arn=self.env_vars.get("COGNITO_USER_POOL_ARN"),
        )

        self.chalice = Chalice(
            self,
            "BaoTranBackend",
            source_dir=RUNTIME_SOURCE_DIR,
            stage_config={
                "lambda_memory_size": 256,
                # "automatic_layer": True,
                "environment_variables": {
                    "APP_TABLE_NAME": self.dynamodb_table.table_name,
                    "ENV": self.ENV,
                    "S3_MAIN_BUCKET": self.bucket.bucket_name,
                    "SQS_GENERIC": self.sqs_generic.queue_arn,
                    "SQS_SENDEMAIL": self.sqs_sendemail.queue_arn,
                    "SNS_MAIN_TOPIC_ARN": "Load from env_vars which is .prod",
                    "COGNITO_USER_POOL_NAME": "Load from env_vars which is .prod",
                    "COGNITO_USER_POOL_ARN": "Load from env_vars which is .prod",
                    "COGNITO_APP_CLIENT_ID": "Load from env_vars which is .prod",
                    # "DYNAMODB_STREAM_ARN": DYNAMODB_STREAM_ARN,  # TODO: get DYNAMODB_STREAM_ARN from table
                }
                | self.env_vars,
                "stages": {
                    self.ENV: {},
                },
            },
        )
        # grant policies
        self.chalice_role = self.chalice.get_role("DefaultRole")

        self.sns_topic.grant_publish(self.chalice_role)
        self.bucket.grant_read_write(self.chalice_role)
        self.bucket.add_event_notification(
            aws_s3.EventType.OBJECT_CREATED_PUT,
            aws_s3_noti.SqsDestination(self.sqs_generic),
        )
        self.dynamodb_table.grant_read_write_data(self.chalice.get_role("DefaultRole"))

        self.sqs_sendemail.grant_consume_messages(self.chalice.get_role("DefaultRole"))
        self.sqs_sendemail.grant_send_messages(self.chalice.get_role("DefaultRole"))
        self.sqs_generic.grant_consume_messages(self.chalice.get_role("DefaultRole"))
        self.sqs_generic.grant_send_messages(self.chalice.get_role("DefaultRole"))

        self.imported_user_pool.grant(
            self.chalice.get_role("DefaultRole"), "cognito-idp:AdminCreateUser"
        )

        # Allow chalice lambda send email with ses
        self.chalice_role.add_to_principal_policy(
            iam.PolicyStatement(
                actions=[
                    "ses:SendEmail",
                    "ses:SendRawEmail",
                    "ses:SendTemplatedEmail",
                    "apigateway:GET",  # allow read api gateway to export swagger
                ],
                resources=["*"],
                effect=iam.Effect.ALLOW,
            )
        )

        # Allow chalice lambda to send ses template
        # for ses_email_template in self.ses_emails_templates:
        #     logger.debug(ses_email_template.get_att("resource.arn").to_string())
        #     self.chalice_role.add_to_principal_policy(
        #         iam.PolicyStatement(
        #             actions=[
        #                 "ses:SendTemplatedEmail",
        #             ],
        #             resources=[ses_email_template.get_att("resource.arn")],
        #             effect=iam.Effect.ALLOW,
        #         )
        #     )

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
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
        )
        cdk.CfnOutput(
            self, f"{self.PREFIX_ID}-table-name", value=dynamodb_table.table_name
        )
        return dynamodb_table

    def _create_sqs(self, id: str, sqs_name: str) -> aws_sqs.Queue:
        # Function timeout <= SQS timeout . Currently function timeout is 60s,
        # TODO: reduce both function timeout and queue timeout
        return aws_sqs.Queue(
            self,
            f"{self.PREFIX_ID}-{id}",
            queue_name=f"{self.PREFIX_NAME}{sqs_name.capitalize()}",
            visibility_timeout=Duration.seconds(60),
        )

    def _create_email_templates(
        self,
        email_template: EmailTemplate,
    ) -> ses.CfnTemplate:
        cfn_template = ses.CfnTemplate(
            self,
            f"{self.PREFIX_NAME}{email_template.template_name}CfnEmailTemplate",
            template=ses.CfnTemplate.TemplateProperty(
                subject_part=email_template.subject_part,
                # the properties below are optional
                html_part=email_template.html_part,
                template_name=f"{self.PREFIX_NAME}_{email_template.template_name}",
                text_part=email_template.text_part,
            ),
        )

        return cfn_template
