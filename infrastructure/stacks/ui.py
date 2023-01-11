import os

from aws_cdk import aws_cloudfront as cf
from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_deployment as s3_deployment

try:
    from aws_cdk import core as cdk
except ImportError:
    import aws_cdk as cdk
UI_SOURCE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), os.pardir, "kycoui", "out"
)


class ReactApp(cdk.Stack):
    """
    example s3 bucket for react-nextjs
    """

    def __init__(self, scope, id, env_vars, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.env_vars = env_vars
        self.PREFIX_NAME = self.env_vars.get("PROJECT_NAME").capitalize()
        self.PREFIX_ID = f"{self.PREFIX_NAME}-ui-id".lower()

        self.site_bucket = s3.Bucket(
            self,
            id=f"{self.PREFIX_ID}-react-build",
            bucket_name=f"kyco-ui-react",
            # public_read_access=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            website_index_document="index.html",
            website_error_document="index.html",
        )

        self.ui_src = s3_deployment.BucketDeployment(
            self,
            f"{self.PREFIX_ID}-react",
            sources=[s3_deployment.Source.asset(UI_SOURCE_DIR)],
            destination_bucket=self.site_bucket,
        )

        self.cloudfront_OAI = cf.OriginAccessIdentity(
            self,
            f"{self.PREFIX_ID}-OAI",
            comment=f"OAI for {self.site_bucket}. only oai can access",
        )

        self.site_bucket_iam_policy = iam.PolicyStatement(
            actions=["s3:GetObject", "s3:PutObject", "s3:PutObjectAcl"],
            resources=[self.site_bucket.arn_for_objects("*")],
            principals=[
                iam.CanonicalUserPrincipal(
                    self.cloudfront_OAI.cloud_front_origin_access_identity_s3_canonical_user_id
                )
            ],
        )

        result = self.site_bucket.add_to_resource_policy(self.site_bucket_iam_policy)

        if not result.statement_added:
            print("Warning: could not add policy")

        # enable certificates if we use DOMAIN_NAME
        # site_certificate = acm_.DnsValidatedCertificate(self, 'siteCert', domain_name=DOMAIN_NAME, region= self.region)
        # viewer_certificate = cloudfront_.ViewerCertificate.from_acm_certificate(
        #     site_certificate,
        #     site_domain=DOMAIN_NAME,
        #     ssl_method=cloudfront_.SSLMethod.SNI,
        #     security_policy=cloudfront_.SecurityPolicyProtocol.TLS_V1_1_2016
        # )

        custom_403 = cf.CfnDistribution.CustomErrorResponseProperty(
            error_code=403,
            error_caching_min_ttl=300,
            response_code=200,
            response_page_path="/404.html",
        )

        custom_404 = cf.CfnDistribution.CustomErrorResponseProperty(
            error_code=404,
            error_caching_min_ttl=300,
            response_code=200,
            response_page_path="/404.html",
        )

        self.public_cfront = cf.CloudFrontWebDistribution(
            self,
            id=f"{self.PREFIX_ID}-distribution",
            origin_configs=[
                {
                    "s3OriginSource": {
                        "s3BucketSource": self.site_bucket,
                        "originAccessIdentity": self.cloudfront_OAI,
                    },
                    "behaviors": [
                        {
                            "isDefaultBehavior": True,
                            "compress": True,
                            "allowedMethods": cf.CloudFrontAllowedMethods.ALL,
                        }
                    ],
                }
            ],
        )
