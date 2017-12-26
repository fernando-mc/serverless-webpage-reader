import boto3
from contextlib import closing

client = boto3.client('polly')

response = client.synthesize_speech(
    OutputFormat='mp3',
    SampleRate='8000',
    Text='All Gaul is divided into three parts',
    TextType='text',
    VoiceId='Joanna',
)

print(response)

with closing(response["AudioStream"]) as stream:
    with open('test.mp3', "wb") as file:
        file.write(stream.read())
        