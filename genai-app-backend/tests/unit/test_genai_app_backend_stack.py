import aws_cdk as core
import aws_cdk.assertions as assertions

from genai_app_backend.genai_app_backend_stack import GenaiAppBackendStack

# example tests. To run these tests, uncomment this file along with the example
# resource in genai_app_backend/genai_app_backend_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = GenaiAppBackendStack(app, "genai-app-backend")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
