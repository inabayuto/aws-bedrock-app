import boto3
import json
import streamlit as st
import botocore
import time

client = boto3.client('bedrock-runtime')

def get_bedrock_response(user_input, retries=5, wait_sec=5):
    body = json.dumps({
        "prompt": f"\n\nHuman: {user_input}\n\nAssistant:",
        "max_tokens_to_sample": 256
    })
    for i in range(retries):
        try:
            response = client.invoke_model(
                modelId='anthropic.claude-v2:1',
                body=body,
                accept='application/json',
                contentType='application/json'
            )
            result = json.loads(response['body'].read())
            return result['completion']
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'ThrottlingException':
                st.write(f"リクエストが多すぎます。{wait_sec}秒待ってリトライします。{e}")
                time.sleep(wait_sec)
            else:
                st.write(f"Error: {e}")
                break
        except Exception as e:
            st.write(f"Error: {e}")
            break
    return None