import textwrap
import boto3
import subprocess 
import os

DURATION_SECONDS = 43200
SERIAL_NUMBER = os.getenv('AWS_SERIAL_NUMBER')

def login(token_code):
    client = boto3.client('sts')
    response = client.get_session_token(
        DurationSeconds=DURATION_SECONDS,
        SerialNumber=SERIAL_NUMBER,
        TokenCode=token_code
    )
 
    access_key = response['Credentials']['AccessKeyId']
    secret_access_key = response['Credentials']['SecretAccessKey']
    session_token = response['Credentials']['SessionToken']
 
    os.environ['AWS_ACCESS_KEY_ID'] = access_key
    os.environ['AWS_SECRET_ACCESS_KEY'] = secret_access_key
    os.environ['AWS_SESSION_TOKEN'] = session_token
 
token_code = input('Enter your token code: ')
login(token_code)
print('login success')