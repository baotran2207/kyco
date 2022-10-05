import os
from unicodedata import name

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


PREFIX_NAME = "chalicecackend"
PREFIX_ID = "chalicecackend-id"

# S3_BUCKET_NAME = "sameple-chalice-glue-sample-output"
# DYNAMODB_STREAM_ARN = "arn:aws:dynamodb:ap-southeast-1:730353997858:table/chalice-backend-AppTable815C50BC-149CVJD33OV2D/stream/2022-08-09T11:28:02.315"


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
                    "POSTGRES_SERVER": "db.xggbesitxdlxuygrlmjk.supabase.co",
                    "POSTGRES_USER": "postgres",
                    "POSTGRES_PASSWORD": "baotran3318!",
                    "POSTGRES_DB": "baotran",
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
