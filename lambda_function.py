import json

def lambda_handler(event, context):
    for record in event['Records']:
        message = json.loads(record['body'])
        print(f"📩 Received message: {message}")

    return {
        'statusCode': 200,
        'body': json.dumps('Message processed successfully')
    }
