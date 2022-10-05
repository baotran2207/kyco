# import os
# from unicodedata import name

# from aws_cdk import (
#     aws_dynamodb as dynamodb,
#     aws_glue_alpha as glue,
#     aws_s3,
#     aws_sns,
#     aws_sqs,
#     aws_glue as glue_stable,
#     aws_cloudwatch as aws_cw,
#     aws_iam as iam_,
# )

# try:
#     from aws_cdk import core as cdk
# except ImportError:
#     import aws_cdk as cdk

# from chalice.cdk import Chalice


# RUNTIME_SOURCE_DIR = os.path.join(
#     os.path.dirname(os.path.dirname(__file__)), os.pardir, "runtime"
# )

# CURDIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))

# GLUE_JOBS_DIR = f"{CURDIR}/assets/glue_jobs"

# PREFIX_NAME = "chalicecackend"
# PREFIX_ID = "chalicecackend-id"

# S3_BUCKET_NAME = "sameple-chalice-glue-sample-output"
# DYNAMODB_STREAM_ARN = "arn:aws:dynamodb:ap-southeast-1:730353997858:table/chalice-backend-AppTable815C50BC-149CVJD33OV2D/stream/2022-08-09T11:28:02.315"

# PUBLIC_SOURCE = "s3://awsglue-datasets/examples/us-legislators/all/"

# GLUE_MANAGED_POLICY = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
# GLUE_SERVICE_URL = "glue.amazonaws.com"


# class ChaliceApp(cdk.Stack):
#     def __init__(self, scope, id, **kwargs):
#         super().__init__(scope, id, **kwargs)
#         # self.dynamodb_table = self._create_ddb_table()

#         self._create_glue_sameple_stack()

#     def _create_glue_sameple_stack(self):
#         self.s3_public_source = aws_s3.Bucket.from_bucket_name(
#             self,
#             id="s3Public",
#             bucket_name="awsglue-datasets"
#             # bucket_name='s3://awsglue-datasets/examples/us-legislators/all/'
#         )

#         self.s3_source_path = f"s3://awsglue-datasets/examples/us-legislators/all"

#         self.s3_source_person_json = f"{self.s3_source_path}/persons.json"
#         self.s3_source_memberships_json = f"{self.s3_source_path}/memberships.json"
#         self.s3_source_organizations_json = f"{self.s3_source_path}/organizations.json"

#         print(self.s3_public_source.bucket_arn)
#         self.s3_output_bucket = aws_s3.Bucket(
#             self,
#             f"{PREFIX_ID}_{S3_BUCKET_NAME}",
#             bucket_name=f"{PREFIX_NAME}-{S3_BUCKET_NAME}",
#         )

#         self.glue_db = glue.Database(
#             self,
#             id=f"{PREFIX_ID}_glue_db",
#             database_name=f"{PREFIX_NAME}_glue_db",
#         )

#         # self.s3_output_bucket.grant_read_write(self.glue_db)

#         self.glue_crawler_role = iam_.Role(
#             self,
#             id="id-glue-crawler-role-example",
#             role_name="AWSGlueServiceRole-allow-insert-db",
#             description="example role for example crawler",
#             managed_policies=[
#                 iam_.ManagedPolicy.from_managed_policy_arn(
#                     self, "glue-service-policy-example", GLUE_MANAGED_POLICY
#                 )
#             ],
#             path="/service-role/",
#             assumed_by=iam_.ServicePrincipal("glue.amazonaws.com"),
#         )  # s3 source is public

#         self.glue_example_role = self.glue_crawler_role


#         self.glue_worlflow = glue_stable.CfnWorkflow(
#             self,
#             "glue-workflow",
#             # default_run_properties=default_run_properties,
#             description="description",
#             name="example_workflow",
#             # tags=tags
#         )
#         self.iam_policy_for_assets = iam_.Policy(
#             self,
#             "id-iam-for-assets",
#             policy_name="glue-policy-workflow-to-access-assets",
#             roles=[self.glue_crawler_role],
#             statements=[
#                 iam_.PolicyStatement(
#                     effect=iam_.Effect.ALLOW,
#                     actions=[
#                         "s3:GetObject",
#                         "s3:PutObject",
#                         "s3:DeleteObject",
#                         "s3:ListBucket",
#                     ],
#                     resources=[self.s3_output_bucket.bucket_arn],
#                 ),
#                 iam_.PolicyStatement(
#                     effect=iam_.Effect.ALLOW,
#                     actions=["s3:GetObject"],
#                     resources=[self.s3_public_source.bucket_arn],
#                 ),
#             ],
#         )

#         self.glue_crawler = glue_stable.CfnCrawler(
#             self,
#             id="glue-stable-crawler-s3",
#             name="glue-stable-crawler-s3-name",
#             role=self.glue_crawler_role.role_name,
#             database_name=self.glue_db.database_name,
#             table_prefix='example',
#             targets=glue_stable.CfnCrawler.TargetsProperty(
#                 s3_targets=[
#                     glue_stable.CfnCrawler.S3TargetProperty(
#                         # connection_name="connectionName",
#                         # dlq_event_queue_arn="dlqEventQueueArn",
#                         # event_queue_arn="eventQueueArn",
#                         # exclusions=["exclusions"],
#                         path=self.s3_source_person_json,
#                         sample_size=123,
#                     )
#                 ]
#             ),
#             schema_change_policy=glue_stable.CfnCrawler.SchemaChangePolicyProperty(
#                 delete_behavior="DEPRECATE_IN_DATABASE", update_behavior="UPDATE_IN_DATABASE"
#             ),

#         )

#         self.glue_job = glue.Job(
#             self,
#             "PythonShellJob",
#             job_name="chalice-example-glue",
#             executable=glue.JobExecutable.python_shell(
#                 glue_version=glue.GlueVersion.V1_0,
#                 python_version=glue.PythonVersion.THREE,
#                 script=glue.Code.from_asset(
#                     f"{GLUE_JOBS_DIR}/examples/join_and_relationalize.py"
#                 ),
#             ),
#             description="an example Python Shell job",
#         )


