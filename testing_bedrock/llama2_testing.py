import os
import json
import boto3
import sys

bedrock = boto3.client("bedrock-runtime")

model_id="meta.llama2-70b-chat-v1"

response = bedrock.invoke_model(
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body = json.loads(response.get("body").read())
response_text = response_body["generation"]
print(response_text)