# bedrock-aws-GenAI
# RAG Using Bedrock

# Streamlit Run
command : streamlit run app.py


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