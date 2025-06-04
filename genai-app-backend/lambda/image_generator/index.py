import boto3
import os
import json
import base64
import uuid

def handler(event, context):
    try:
        # Parse the request body
        prompt = event.get("prompt", "A beautiful landscape with mountains and a lake")
        
        # Get model ID from environment variable or use default
        model_id = os.environ.get("BEDROCK_IMAGE_MODEL_ID", "amazon.nova-canvas-v1:0")
        
        # Initialize Bedrock runtime client
        client = boto3.client('bedrock-runtime')
        
        # Prepare request body for Amazon Nova Canvas
        request_body = {
            "prompt": prompt,
            "negativePrompt": "",  # Optional negative prompt
            "imageGenerationConfig": {
                "numberOfImages": 1,
                "height": 1024,
                "width": 1024,
                "cfgScale": 8.0,  # Controls how closely the image follows the prompt
                "seed": int(uuid.uuid4().int % 2147483647)  # Random seed
            }
        }
        
        # Invoke the model
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body)
        )
        
        # Parse the response
        response_body = json.loads(response['body'].read())
        
        # Extract the base64-encoded image from Nova Canvas response
        image_base64 = response_body.get('images', [''])[0]
        
        # Return the response with CORS headers
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({
                "image": image_base64,
                "prompt": prompt
            })
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }
