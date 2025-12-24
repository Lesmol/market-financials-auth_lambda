import boto3
import json
import os
from botocore.exceptions import ClientError

dynamodb = boto3.resource("dynamodb")

TABLE_NAME = os.environ.get("DYNAMODB_AUTH_TABLE_NAME")
table = dynamodb.Table(TABLE_NAME)

def handler(event, context):
    print(f"Starting: {json.dump(event)}")
    headers = event.get("headers", {})
    apikey = headers.get("x-api-key")
    
    if not apikey:
        return { "isAuthorized": False }
    
    try:
        response = table.get_item(
            Key = {
                "ApiKey": apikey
            }
        )
        
        if "Item" in response:
            return { "isAuthorized": True }
        else:
            return { "isAuthorized": False }
    except Exception as ex:
        print(f"Exception: {ex}")
        return { "isAuthorized": False }
