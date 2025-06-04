# GenAI App Backend

This project implements a serverless backend for a generative AI application using AWS CDK, AWS Lambda, Amazon API Gateway, and Amazon Bedrock. The backend provides APIs for both text and image generation using Amazon's foundation models.

## Architecture

The application consists of the following components:

- **AWS Lambda Functions**:
  - Text Generation: Uses Amazon Nova Lite model to generate text responses
  - Image Generation: Uses Amazon Nova Canvas model to create images from text prompts

- **Amazon API Gateway**: Provides RESTful endpoints to interact with the Lambda functions
  - `/text` endpoint for text generation
  - `/image` endpoint for image generation

- **Amazon Bedrock**: Provides the foundation models for AI generation
  - Nova Lite (text generation)
  - Nova Canvas (image generation)

## Prerequisites

- AWS Account with access to Amazon Bedrock
- Python 3.12 or higher
- AWS CDK v2 installed
- Proper AWS credentials configured

## Setup

1. **Create and activate a virtual environment**:

   ```bash
   # For MacOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate

   # For Windows
   python -m venv .venv
   .venv\Scripts\activate.bat
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Bootstrap CDK (if not already done)**:

   ```bash
   cdk bootstrap
   ```

4. **Deploy the stack**:

   ```bash
   cdk deploy
   ```

## API Usage

### Text Generation

Send a POST request to the `/text` endpoint with a JSON payload:

```json
{
  "prompt": "Write a short story about dragons"
}
```

The response will contain the generated text:

```json
{
  "statusCode": 200,
  "body": "In the heart of the ancient mountains, where the clouds kissed the peaks..."
}
```

### Image Generation

Send a POST request to the `/image` endpoint with a JSON payload:

```json
{
  "prompt": "A beautiful landscape with mountains and a lake"
}
```

The response will contain a base64-encoded image:

```json
{
  "statusCode": 200,
  "body": {
    "image": "base64_encoded_image_data",
    "prompt": "A beautiful landscape with mountains and a lake"
  }
}
```

## Project Structure

```
genai-app-backend/
├── genai_app_backend/
│   └── genai_app_backend_stack.py  # CDK stack definition
├── lambda/
│   ├── orchestrator/               # Text generation Lambda
│   │   └── index.py
│   └── image_generator/            # Image generation Lambda
│       └── index.py
├── app.py                          # CDK app entry point
├── cdk.json                        # CDK configuration
└── requirements.txt                # Python dependencies
```

## Lambda Functions

### Text Generation (orchestrator)

The text generation Lambda uses Amazon Bedrock's Nova Lite model to generate text responses based on user prompts. It configures the model with appropriate parameters for temperature, top-p, and maximum tokens.

### Image Generation (image_generator)

The image generation Lambda uses Amazon Bedrock's Nova Canvas model to create images from text descriptions. It supports customization of image dimensions, configuration parameters, and returns base64-encoded images.

## IAM Permissions

The Lambda functions use an IAM role with the following permissions:
- `AWSLambdaBasicExecutionRole` for CloudWatch Logs access
- Custom policy for Bedrock model invocation (`bedrock:InvokeModel`, `bedrock-runtime:InvokeModel`)

## Useful Commands

- `cdk ls` - List all stacks in the app
- `cdk synth` - Emit the synthesized CloudFormation template
- `cdk deploy` - Deploy this stack to your default AWS account/region
- `cdk diff` - Compare deployed stack with current state
- `cdk docs` - Open CDK documentation

## Customization

You can customize the models and parameters by modifying the environment variables in the CDK stack:

- `BEDROCK_MODEL_ID` for the text generation model
- `BEDROCK_IMAGE_MODEL_ID` for the image generation model

## Security Considerations

- The API Gateway endpoints are publicly accessible but can be restricted using API keys or other authorization methods
- The Lambda functions have minimal IAM permissions following the principle of least privilege
- CORS is enabled to allow cross-origin requests from web applications

## Cost Considerations

- Amazon Bedrock charges based on the number of input and output tokens for text models
- Image generation is charged per image based on resolution
- Lambda and API Gateway have their own pricing based on requests and execution time
