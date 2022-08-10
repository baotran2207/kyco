from pydantic import BaseSettings,  validator, SecretStr, HttpUrl, PostgresDsn
from typing import Optional, Any, Dict
import os


class AppSettings(BaseSettings):

    # Init User
    WEBMASTER_EMAIL: str = os.getenv("WEBMASTER_EMAIL")
    WEBMASTER_PASSWORD: str = os.getenv("WEBMASTER_PASSWORD")

    # DB
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, val: Optional[str], values: Dict[str, Any]) -> Any:

        if isinstance(val, str):
            return val
        if not values.get("POSTGRES_SERVER") :
            return val

        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    # Security
    secret_key: SecretStr = os.getenv("SecretStr")
    jwt_token_prefix: str = "Token"  # token? Bearer ?

    # sentry
    SENTRY_DSN: Optional[HttpUrl] = os.getenv("SENTRY_DSN")

    @validator("SENTRY_DSN", pre=True)
    def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
        if not v : return v
        if len(v) == 0:
            return None
        return v

    # databrick
    DATABRICKS_WORKSPACE_URL: HttpUrl = os.getenv("DATABRICKS_WORKSPACE_URL")
    DATABRICKS_TOKEN: str = os.getenv("DATABRICKS_TOKEN")
    DATABRICKS_JOB_API_VERSION: str = os.getenv("DATABRICKS_JOB_API_VERSION")


    # Dynamo
    DYNAMO_TABLE_NAME:str = os.environ.get('APP_TABLE_NAME', '')
    DYNAMODB_STREAM_ARN:str = os.environ.get('DYNAMODB_STREAM_ARN', '')


settings = AppSettings()