from aws_cdk import (
    Duration,
    aws_lambda as lambda_,
    aws_iam as iam,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class GenaiAppBackendStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_retrieval_role = iam.Role(self, "LambdaRetrievalRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"),
            ],
            description="Role for Lambda to connect to Bedrock and invoke models",
        )

        bedrock_policy_statement = iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=["bedrock:invokeModel"],
            resources=["*"],
        )

        lambda_retrieval_role.add_to_policy(bedrock_policy_statement)

        fn = lambda_.Function(self, "Orchestration",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="index.handler",
            code=lambda_.Code.from_asset("lambda/orchestrator"),
            timeout=Duration.seconds(45),
            memory_size=128,
            role=lambda_retrieval_role,
            environment={
                "BEDROCK_MODEL_ID": "us.amazon.nova-lite-v1:0",
            }
        )
