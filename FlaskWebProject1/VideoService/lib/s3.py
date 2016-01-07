from flask import current_app as app
from boto.s3.key import Key
from boto.s3.connection import OrdinaryCallingFormat, S3Connection
import boto3
import botocore 
import boto


def upload_video_to_s3(bucket_name, source_path, s3_path):
    s3 = boto3.resource('s3',
                        aws_access_key_id = 'AKIAJ6DLWSW52NGKCFDQ',
                        aws_secret_access_key = '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')
    
    #get the bucket
    bucket = s3.Bucket(name = bucket_name)
    try: 
        bucket.upload_file(source_path, 'key')
    except botocore.exceptions.ClientError as e: 
        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.
        error_code = int(e.response['Error']['Code']) 
        
        

        