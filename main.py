import boto3
import json


brt = boto3.client(
    service_name='bedrock-runtime', 
    region_name='us-east-1')

body = json.dumps({
    "prompt": "\n\n Human: カレーの作り方を教えてください。\n\nAssistant:",
    "max_tokens_to_sample": 300,
    "temperature": 0.1,
    "top_p": 0.9,
})

modelId = 'anthropic.claude-instant-v1'
accept = 'application/json'
contentType = 'application/json'

response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

response_body = json.loads(response.get('body').read())

# text
print(response_body.get('completion'))
