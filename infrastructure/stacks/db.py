from aws_cdk import core as cdk

from aws_cdk import (
    aws_dynamodb as dynamodb,  # aws_ses as ses,; aws_sns,;; aws_cloudwatch as aws_cw,;;
)


class KycoDB(cdk.Stack):
    """
    Init dynamodb and export to chalcie app
    """

    def __init__(self, scope, id, env_vars, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.env_vars = env_vars

        self.kycodb = self._create_table()

    def _create_table(self):
        dynamodb_table = dynamodb.Table(
            self,
            f"{self.PREFIX_ID}-kyco",
            partition_key=dynamodb.Attribute(
                name="PK", type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(name="SK", type=dynamodb.AttributeType.STRING),
            stream=dynamodb.StreamViewType.NEW_IMAGE,
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )
        cdk.CfnOutput(
            self, f"{self.PREFIX_ID}-kyco-cfn", value=dynamodb_table.table_name
        )
        return dynamodb_table
