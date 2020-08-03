import boto3
import json

def handler(event, context):
    response = "Hi, my name is Brooke."
    return {
        'statusCode': 200,
        'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        },
        'body': json.dumps(response)
        }
    
    
    