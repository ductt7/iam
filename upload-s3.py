import boto3

s3 = boto3.client( 's3', aws_access_key_id='<ACCESSKEY>', aws_secret_access_key='<SECRETACCESSKEY>')
s3.upload_file('test-s3.txt', '<S3BUCKETNAME>', 'test-s3.txt')