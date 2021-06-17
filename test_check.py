import boto3
import os

ACCESS_KEY = '*'
SECRET_ACCESS_KEY = '*'


client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_ACCESS_KEY
)

print(vars(client))


upload_file_bucket = 'upload-file-bucket-jpd'
for file in os.listdir():
    if '.py' in file:
        upload_file_key = 'fold1/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
