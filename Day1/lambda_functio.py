import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tank-updates-yogeshwar')  

def lambda_handler(event, context):
    try:
        params = event.get('queryStringParameters') or {}
        device_id = params.get('device_id')
        value = params.get('value')

        if not device_id or not value:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing device_id or value"})
            }

        
        table.put_item(Item={
            'unique_id': device_id,
            'value': value
        })

       
        response = table.get_item(Key={'unique_id': device_id})
        item = response.get('Item', {})

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Data saved and fetched successfully!",
                "data": item
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

