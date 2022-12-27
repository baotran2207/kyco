import boto3
from chalicelib.config import settings

dynamodb = boto3.resource("dynamodb")
dynamodb_table = dynamodb.Table(settings.DYNAMO_TABLE_NAME)
