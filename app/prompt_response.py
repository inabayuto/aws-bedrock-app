import boto3
import json

def get_response(body):

    brt = boto3.client(
    service_name='bedrock-runtime', 
    region_name='us-east-1')
    
    modelId = 'anthropic.claude-v2'
    accept = 'application/json'
    contentType = 'application/json'
    
    response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    
    response_body = json.loads(response.get('body').read())
    
    # text
    return response_body.get('completion')

def get_response_with_prompt(prompt):
    
    body = json.dumps({
        "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
        "max_tokens_to_sample": 300,
        "temperature": 0.1,
        "top_p": 0.9,
    })
    return get_response(body)