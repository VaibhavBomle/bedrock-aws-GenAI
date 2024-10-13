import os
import json
import boto3
import sys

# Initiaize bedrock client
bedrock = boto3.client("bedrock-runtime")

#Prompt
prompt="""

        you are a AI expert now just tell me Which company best for AI Innnovation?
"""
# Defining paylload
payload={
    
    "prompt": "[INST]"+prompt+"[/INST]",
    "max_gen_len": 512,
    "temperature": 0.3,
    "top_p":0.9
}

# Creating payload in josn
body=json.dumps(payload)
model_id="meta.llama2-70b-chat-v1"

# Note : you need to configure key before calling bedrock from terminal
# command : aws configure  
# Then pass AWS key secret

"""
Or You can create bedrock client as shown below
bedrock = boto3.client(
    'bedrock-runtime',
    aws_access_key_id='your-access-key-id',
    aws_secret_access_key='your-secret-access-key',
    region_name='your-region'
)

"""

# invoking bedrock by passing parameter
response = bedrock.invoke_model(
    body = body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body = json.loads(response.get("body").read())
response_text = response_body["generation"]
print(response_text)