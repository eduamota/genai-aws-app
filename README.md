# AWS Bedrock Foundation Models Demo

A comprehensive project demonstrating how to integrate and utilize AWS Bedrock foundation models for AI-powered applications, with practical examples using operational machinery data.

## Overview

This project showcases the capabilities of AWS Bedrock, Amazon's fully managed service that offers foundation models from leading AI companies. The repository includes practical examples of model integration, data analysis workflows, and operational insights generation using Amazon's Nova and Titan model families.

## Features

- **Foundation Model Integration**: Connect to and utilize various AWS Bedrock models
- **Operational Data Analysis**: Process and analyze machinery operational data
- **Multi-Modal Support**: Examples with text, image, and video capable models
- **Interactive Notebooks**: Jupyter notebooks for hands-on experimentation
- **Real-World Data**: Sample operational dataset for practical learning

## Project Structure

```
├── data/
│   └── sample_operational.csv    # Sample machinery operational data
├── 01_Bedrock_SDK.ipynb         # Basic Bedrock SDK usage and model interaction
├── 02_Bedrock_With_Data.ipynb   # Data analysis with Bedrock models
└── requirements.txt             # Python dependencies
```

## Available Models

The project demonstrates integration with various Amazon Bedrock models:

### Amazon Nova Family
- **Nova Pro**: Multi-modal model (text, image, video input)
- **Nova Lite**: Efficient multi-modal model
- **Nova Micro**: Lightweight text-only model
- **Nova Sonic**: Speech-to-text and text-to-speech model

### Amazon Titan Family
- **Titan Text Premier**: Advanced text generation
- **Titan Text Express**: Fast text processing
- **Titan Text Lite**: Efficient text generation
- **Titan Text Large**: Comprehensive text model

## Sample Data

The included `sample_operational.csv` contains machinery operational data with the following fields:
- `machine_id`: Equipment identifier
- `operation_date`: Date of operation
- `hours_operated`: Daily operational hours
- `fuel_consumed_liters`: Fuel consumption
- `idle_time_hours`: Equipment idle time
- `material_moved_cubic_meters`: Material handling volume
- `maintenance_flag`: Maintenance status indicator

## Prerequisites

- Python 3.8 or higher
- AWS Account with Bedrock access
- AWS CLI configured with appropriate credentials
- Jupyter Notebook environment

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd aws-bedrock-demo
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS credentials**
   ```bash
   aws configure
   ```
   
   Or set environment variables:
   ```bash
   export AWS_ACCESS_KEY_ID=your_access_key
   export AWS_SECRET_ACCESS_KEY=your_secret_key
   export AWS_DEFAULT_REGION=us-east-1
   ```

## AWS Bedrock Setup

### Model Access Request
Before using Bedrock models, you need to request access:

1. Navigate to AWS Bedrock console
2. Go to "Model access" in the left sidebar
3. Select the models you want to use
4. Submit access requests (approval may take time)

### Required IAM Permissions
Ensure your AWS user/role has the following permissions:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:ListFoundationModels",
                "bedrock:GetFoundationModel",
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream"
            ],
            "Resource": "*"
        }
    ]
}
```

## Usage

### Basic Model Interaction

```python
import boto3
import json

# Initialize Bedrock clients
bedrock_client = boto3.client('bedrock')
bedrock_runtime = boto3.client('bedrock-runtime')

# List available models
response = bedrock_client.list_foundation_models(
    byProvider='Amazon',
    byOutputModality='TEXT'
)

# Use a model
model_id = 'us.amazon.nova-lite-v1:0'
messages = [{
    "role": "user", 
    "content": [{"text": "Analyze this operational data..."}]
}]

response = bedrock_runtime.converse(
    modelId=model_id,
    messages=messages,
    inferenceConfig={
        "maxTokens": 500,
        "temperature": 0.7,
        "topP": 0.9
    }
)
```

### Running the Notebooks

1. **Start Jupyter**
   ```bash
   jupyter notebook
   ```

2. **Open notebooks in order:**
   - `01_Bedrock_SDK.ipynb`: Learn basic Bedrock integration
   - `02_Bedrock_With_Data.ipynb`: Explore data analysis capabilities

## Use Cases

### Operational Analytics
- **Predictive Maintenance**: Analyze patterns to predict equipment failures
- **Efficiency Optimization**: Identify opportunities to improve operational efficiency
- **Anomaly Detection**: Detect unusual patterns in machinery behavior
- **Cost Analysis**: Generate insights on fuel consumption and operational costs

### Business Intelligence
- **Report Generation**: Create automated operational reports
- **Data Summarization**: Summarize complex operational datasets
- **Trend Analysis**: Identify long-term operational trends
- **Performance Insights**: Generate actionable performance recommendations

## Model Configuration

### Inference Parameters
- **maxTokens**: Maximum response length (100-4096)
- **temperature**: Creativity/randomness (0.0-1.0)
- **topP**: Nucleus sampling threshold (0.0-1.0)

### Best Practices
- Start with lower temperature (0.1-0.3) for analytical tasks
- Use higher temperature (0.7-1.0) for creative content
- Adjust maxTokens based on expected response length
- Monitor token usage for cost optimization

## Cost Considerations

- **Input Tokens**: Charged per 1,000 input tokens
- **Output Tokens**: Charged per 1,000 output tokens
- **Model Pricing**: Varies by model (Nova models generally more cost-effective)
- **Optimization**: Use appropriate model size for your use case

## Troubleshooting

### Common Issues

1. **Access Denied**
   - Ensure model access is approved in Bedrock console
   - Verify IAM permissions
   - Check AWS region availability

2. **Model Not Found**
   - Confirm model ID format
   - Verify model availability in your region
   - Check model lifecycle status

3. **Rate Limiting**
   - Implement exponential backoff
   - Monitor usage quotas
   - Consider batch processing

### Debug Tips
- Enable detailed logging
- Check AWS CloudTrail for API calls
- Validate request format and parameters
- Test with minimal examples first

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests and documentation
5. Submit a pull request

## Resources

- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/)
- [Model Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html)
- [Pricing Information](https://aws.amazon.com/bedrock/pricing/)
- [Best Practices](https://docs.aws.amazon.com/bedrock/latest/userguide/best-practices.html)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions and support:
- AWS Bedrock Documentation
- AWS Support Center
- Community forums and GitHub issues

---

**Note**: This project is for educational and demonstration purposes. Ensure compliance with AWS usage policies and your organization's data governance requirements when working with production data.