#!/usr/bin/python
# Create a role.
# Create a Lambda function.

import json
import io
import time
import zipfile
from uuid import uuid4

import boto3
import botocore


def create_lambda_deployment_package(file_name) -> bytes:
    """
    Creates a Lambda deployment package in ZIP format in an in-memory buffer.
    @param file_name: file containing source code
    @return: bytes
    """
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as zipped:
        zipped.write(file_name)
    buffer.seek(0)
    return buffer.read()


def main():
    region = "us-east-1"

    function_name = f"RomanNumbersConverter-{uuid4()}"
    function_file = "../lambda/hello.py"
    function_handler = "handler"
    lambda_policy = {
            "Version": "2012-10-17",
            "Statement": {
                "Effect": "Allow",
                "Principal": {"Service": "lambda.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }
        }

    iam_resource = boto3.resource("iam")
    lambda_client = boto3.client("lambda", region_name=region)

    try:
        # Create role
        role = iam_resource.create_role(
            RoleName=f"ogre-role-{uuid4()}",
            AssumeRolePolicyDocument=json.dumps(lambda_policy))

        # Wait for role to be created
        time.sleep(10)

        deployment_package = create_lambda_deployment_package(function_file)
        # Create Lambda function
        response = lambda_client.create_function(
            FunctionName=function_name,
            Description="Demo lambda for OGRE",
            Runtime="python3.9",
            Role=role.arn,
            Handler=function_handler,
            Code={"ZipFile": deployment_package},
            Publish=True)

        print(f'Response: {response}')
        function_arn = response["FunctionArn"]
        print(f'\nCreated function {function_name} with ARN: {function_arn}')

    except botocore.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "AccessDeniedException":
            print("Error: Access Denied!!")
        elif e.response["Error"]["Code"] == "ValidationException":
            print("Error: Name Not Valid!!")
        else:
            raise


if __name__ == '__main__':
    main()
