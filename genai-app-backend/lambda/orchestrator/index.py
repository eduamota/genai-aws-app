import boto3
import os

def handler(event, context):

    user_prompt = event.get("prompt", "Write a short story about dragons")

    modelId = os.environ.get("BEDROCK_MODEL_ID", "us.amazon.nova-lite-v1:0")
    client_runtime = boto3.client("bedrock-runtime")
    system = [{ "text": "You are a helpful assistant" }]

    messages = [
        {"role": "user", "content": [{"text": user_prompt}]},
    ]

    inf_params = {"maxTokens": 300, "topP": 0.99, "temperature": 1}

    model_response = client_runtime.converse(
        modelId=modelId, 
        messages=messages, 
        system=system, 
        inferenceConfig=inf_params
    )

    output = model_response["output"]["message"]["content"][0]["text"]

    print(output)
    return {"statusCode": 200, "body": output}