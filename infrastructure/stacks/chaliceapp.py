import os
from unicodedata import name

from aws_cdk import (
    aws_dynamodb as dynamodb,
    aws_glue_alpha as glue,
    aws_s3,
    aws_sns,
    aws_sqs,
    aws_cloudwatch as aws_cw,
)

try:
    from aws_cdk import core as cdk
except ImportError:
    import aws_cdk as cdk

from chalice.cdk import Chalice


RUNTIME_SOURCE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), os.pardir, "runtime"
)

CURDIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__))
)

GLUE_JOBS_DIR = f"{CURDIR}/assets/glue_jobs"

PREFIX_NAME = "chalicecackend"
PREFIX_ID = "chalicecackend-id"

S3_BUCKET_NAME = "sameple-chalice-glue-sample-output"
DYNAMODB_STREAM_ARN = "arn:aws:dynamodb:ap-southeast-1:730353997858:table/chalice-backend-AppTable815C50BC-149CVJD33OV2D/stream/2022-08-09T11:28:02.315"

PUBLIC_SOURCE = "s3://awsglue-datasets/examples/us-legislators/all/"

class ChaliceApp(cdk.Stack):
    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)
        self.dynamodb_table = self._create_ddb_table()
        self.chalice = Chalice(
            self,
            "ChaliceApp",
            source_dir=RUNTIME_SOURCE_DIR,
            stage_config={
                "environment_variables": {
                    "APP_TABLE_NAME": self.dynamodb_table.table_name,
                    "DYNAMODB_STREAM_ARN": DYNAMODB_STREAM_ARN,  # TODO: get DYNAMODB_STREAM_ARN from table
                }
            },
        )
        self.dynamodb_table.grant_read_write_data(self.chalice.get_role("DefaultRole"))


        self._create_glue_sameple_stack()

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


    def _create_glue_sameple_stack(self):
        self.s3_output_bucket = aws_s3.Bucket(
            self,
            f"{PREFIX_ID}_{S3_BUCKET_NAME}",
            bucket_name=f"{PREFIX_NAME}-{S3_BUCKET_NAME}",
        )

        self.glue_db = glue.Database(
            self,
            id=f"{PREFIX_ID}_glue_db",
            database_name=f"{PREFIX_NAME}_glue_db",
        )

        self.glue_job = glue.Job(
            self,
            "PythonShellJob",
            job_name="chalice-example-glue",
            executable=glue.JobExecutable.python_shell(
                glue_version=glue.GlueVersion.V1_0,
                python_version=glue.PythonVersion.THREE,
                script=glue.Code.from_asset(
                    f"{GLUE_JOBS_DIR}/examples/join_and_relationalize.py"
                ),
            ),
            description="an example Python Shell job",
        )

        # tbl_persons = "persons_json"
        # tbl_membership = "memberships_json"
        # tbl_organization = "organizations_json"

        self.glue_db_table_persons_json = glue.Table(
            self,
            f"{PREFIX_ID}_persons_json",
            database=self.glue_db,
            table_name="persons_json",
            data_format=glue.DataFormat.JSON,
            columns=[]
        )

        self.glue_db_table_memberships_json = glue.Table(
            self,
            f"{PREFIX_ID}_memberships_json",
            database=self.glue_db,
            table_name="memberships_json",
            data_format=glue.DataFormat.JSON,
            columns=[]
        )

        self.glue_db_table_organizations_json = glue.Table(
            self,
            f"{PREFIX_ID}_organizations_json",
            database=self.glue_db,
            table_name="organizations_json",
            data_format=glue.DataFormat.JSON,
            columns=[]
        )

        self.s3_output_bucket.grant_read_write(self.glue_db)
