import json
import logging
import os
from typing import Any, Dict, Optional

import boto3
from chalice import CORSConfig
from chalicelib.enums import AppEnv
from pydantic import HttpUrl, PostgresDsn, validator

try:
    from pydantic_settings import BaseSettings
except:
    from pydantic import BaseSettings
ENV = os.environ.get("ENV", "dev")

if ENV == "dev":
    from dotenv import load_dotenv

    load_dotenv("../.dev")

if ENV == "test":
    from dotenv import load_dotenv

    load_dotenv("../.test")


def get_ssm_object(name) -> dict:
    ssm_client = boto3.client("ssm")
    parameter = ssm_client.get_parameter(Name=name)
    return json.loads(parameter["Parameter"]["Value"])


class AppSettings(BaseSettings):
    PROJECT_NAME: str = os.environ.get("PROJECT_NAME", "kyco")
    ENV: str = os.environ["ENV"]
    # Init User
    WEBMASTER_EMAIL: str = os.environ.get("WEBMASTER_EMAIL")
    WEBMASTER_PASSWORD: str = os.environ.get("WEBMASTER_PASSWORD")
    # DB
    POSTGRES_SERVER: Optional[str] = os.environ.get("POSTGRES_SERVER")
    POSTGRES_USER: Optional[str] = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: Optional[str] = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_DB: Optional[str] = os.environ.get("POSTGRES_DB")
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, val: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(val, str):
            return val
        if not values.get("POSTGRES_SERVER"):
            return val

        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    # redis
    REDIS_URL: Optional[str] = os.environ.get("REDIS_URL", "")
    # Security
    COGNITO_USER_POOL_NAME: str = os.environ.get("COGNITO_USER_POOL_NAME", "")
    COGNITO_USER_POOL_ARN: str = os.environ.get("COGNITO_USER_POOL_ARN", "")
    COGNITO_USER_POOL_ID: str = (
        COGNITO_USER_POOL_ARN and COGNITO_USER_POOL_ARN.split("/")[-1] or ""
    )
    COGNITO_APP_CLIENT_ID: str = os.environ.get("COGNITO_APP_CLIENT_ID", "")
    secret_key: str = os.environ.get("SecretStr")
    jwt_token_prefix: str = "Token"  # token? Bearer ?

    # sentry
    SENTRY_DSN: Optional[HttpUrl] = os.environ.get("SENTRY_DSN")

    @validator("SENTRY_DSN", pre=True)
    def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
        if not v:
            return v
        if len(v) == 0:
            return None
        return v

    # databrick
    # DATABRICKS_WORKSPACE_URL: HttpUrl = env_vars.get("DATABRICKS_WORKSPACE_URL")
    # DATABRICKS_TOKEN: str = env_vars.get("DATABRICKS_TOKEN")
    # DATABRICKS_JOB_API_VERSION: str = env_vars.get("DATABRICKS_JOB_API_VERSION")

    # Dynamo
    DYNAMO_TABLE_NAME: str = os.environ.get("APP_TABLE_NAME", "")
    DYNAMODB_STREAM_ARN: str = os.environ.get("DYNAMODB_STREAM_ARN", "")

    # s3
    S3_MAIN_BUCKET: str = os.environ.get("S3_MAIN_BUCKET", "")
    # SQS
    SQS_GENERIC: Optional[str] = os.environ.get("SQS_GENERIC", "")
    SQS_GENERIC_NAME: Optional[str] = os.environ.get("SQS_GENERIC_NAME")

    @validator("SQS_GENERIC_NAME", pre=False)
    def set_sqs_generic_name(cls, val: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(val, str):
            return val

        sqs_name = values.get("SQS_GENERIC")
        return sqs_name and sqs_name.split(":")[-1] or None

    SQS_SENDEMAIL: Optional[str] = os.environ.get("SQS_SENDEMAIL", "")
    SQS_DEADLETTER: Optional[str] = os.environ.get("SQS_DEADLETTER", "")

    # SNS
    SNS_MAIN_TOPIC_ARN: Optional[str] = os.environ.get("SNS_MAIN_TOPIC_ARN")
    SNS_MAIN_TOPIC_NAME: Optional[str] = os.environ.get("SNS_MAIN_TOPIC_NAME")

    @validator("SNS_MAIN_TOPIC_NAME", pre=False)
    def set_sns_topic_name(cls, val: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(val, str):
            return val

        sns_arn = values.get("SNS_MAIN_TOPIC_ARN")
        return sns_arn and sns_arn.split(":")[-1] or None

    # GITHUB
    GITHUB_TOKEN: Optional[str] = os.environ.get("GITHUB_TOKEN")

    # logging
    LOGGING_LEVEL: Optional[str] = None

    @validator("LOGGING_LEVEL", pre=False)
    def set_logging_level(cls, val: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(val, str):
            return val

        env = values.get("ENV")
        if env == AppEnv.dev.value:
            return logging.DEBUG
        return logging.INFO

    # binance
    BINANCE_API_KEY: str = os.environ.get("BINANCE_API_KEY")
    BINANCE_API_SECRET: str = os.environ.get("BINANCE_API_SECRET")

    # TELEGRAM_BOT_TOKEN
    TELEGRAM_BOT_TOKEN: str = os.environ.get("TELEGRAM_BOT_TOKEN")


cors_config = CORSConfig(
    allow_origin="*",
    # allow_headers=["X-Special-Header"],
    max_age=600,
    # expose_headers=["X-Special-Header"],
    allow_credentials=True,
)


settings = AppSettings()
