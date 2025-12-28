import boto3
import json
import os

TABLE_NAME = os.environ.get("DYNAMODB_AUTH_TABLE_NAME")

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)

def is_authorized():
    return { "isAuthorized": True }

def not_authorzed():
    return { "isAuthorized": False }

def handler(event, context):
    try:
        print(f"Starting: {json.dumps(event)}")
        headers = event.get("headers", {})
        apikey = headers.get("x-api-key")
        
        if not apikey:
            return not_authorzed()
    
        response = table.get_item(
            Key = {
                "ApiKey": apikey
            }
        )
        
        if "Item" in response:
            return is_authorized()
        
        return not_authorzed()
    except Exception as ex:
        print(f"Exception: {ex}")
        return not_authorzed()
