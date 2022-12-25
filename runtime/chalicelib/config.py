import json
import os
from typing import Any, Dict, Optional

import boto3
from pydantic import BaseSettings, HttpUrl, PostgresDsn, SecretStr, validator

ssm_name = os.getenv("SSM_NAME")


def get_ssm_object(name) -> dict:
    ssm_client = boto3.client("ssm")
    parameter = ssm_client.get_parameter(Name=name)
    return json.loads(parameter["Parameter"]["Value"])


env_vars = get_ssm_object(ssm_name)


def _get_env_from_os_or_ssm(env_key):
    return os.environ.get(env_key, "") or env_vars.get(env_key)


class AppSettings(BaseSettings):
    ENV: str = env_vars.get("ENV")

    # Init User
    WEBMASTER_EMAIL: str = _get_env_from_os_or_ssm("WEBMASTER_EMAIL")
    WEBMASTER_PASSWORD: str = _get_env_from_os_or_ssm("WEBMASTER_PASSWORD")
    # DB
    POSTGRES_SERVER: str = env_vars.get("POSTGRES_SERVER")
    POSTGRES_USER: str = env_vars.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = env_vars.get("POSTGRES_PASSWORD")
    POSTGRES_DB: str = env_vars.get("POSTGRES_DB")
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

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
    REDIS_URL = env_vars.get("REDIS_URL", "")
    # Security
    COGNITO_USER_POOL = _get_env_from_os_or_ssm("COGNITO_USER_POOL")
    COGNITO_USER_POOL_ID = COGNITO_USER_POOL and COGNITO_USER_POOL.split("/")[-1]
    COGNITO_APP_CLIENT_ID = _get_env_from_os_or_ssm("COGNITO_APP_CLIENT_ID")
    secret_key: SecretStr = env_vars.get("SecretStr")
    jwt_token_prefix: str = "Token"  # token? Bearer ?

    # sentry
    SENTRY_DSN: Optional[HttpUrl] = env_vars.get("SENTRY_DSN")

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
    SQS_GENERIC = os.environ.get("SQS_GENERIC", "")
    SQS_SENDEMAIL = os.environ.get("SQS_SENDEMAIL", "")
    SQS_DEADLETTER = os.environ.get("SQS_DEADLETTER", "")

    # GITHUB
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")


settings = AppSettings()
