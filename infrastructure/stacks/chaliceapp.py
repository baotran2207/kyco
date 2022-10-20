import os
from unicodedata import name
import json
from aws_cdk import (
    aws_dynamodb as dynamodb,
    aws_s3,
    aws_sns,
    aws_sqs,
    aws_cloudwatch as aws_cw,
    aws_iam as iam_,
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

SECREC_FILE_PATH = os.path.join(
    CURDIR,"assets", "ssm_parameter_store", "prod.json"
)

PREFIX_NAME = "chalicecackend"
PREFIX_ID = "chalicecackend-id"


def get_config_secret(SECREC_FILE_PATH):
    f = open(SECREC_FILE_PATH)


    ssm_config = json.load(f)
    print(ssm_config)
    return ssm_config

get_config_secret(SECREC_FILE_PATH)
import aws_cdk.aws_ssm as ssm
class ChaliceApp(cdk.Stack):
    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)
        self.dynamodb_table = self._create_ddb_table()
        self.chalice = Chalice(
            self,
            "BaoTranBackend",
            source_dir=RUNTIME_SOURCE_DIR,
            stage_config={
                "environment_variables": {
                    "APP_TABLE_NAME": self.dynamodb_table.table_name,
                    "ENV": "prod",
                    "SSM_NAME": "/chalice_backend/prod",
                    # "DYNAMODB_STREAM_ARN": DYNAMODB_STREAM_ARN,  # TODO: get DYNAMODB_STREAM_ARN from table
                }
            },
        )
        self.dynamodb_table.grant_read_write_data(self.chalice.get_role("DefaultRole"))

    def _create_ddb_table(self):
        dynamodb_table = dynamodb.Table(
            self,
            "AppTable",
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
        ssm.StringParameter(self, "Parameter",
            allowed_pattern=".*",
            description="The value Foo",
            parameter_name="FooParameter",
            string_value="Foo",
            tier=ssm.ParameterTier.ADVANCED
        )
