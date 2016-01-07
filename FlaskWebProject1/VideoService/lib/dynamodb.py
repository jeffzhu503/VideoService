from flask import current_app as app
from boto.s3.key import Key
from boto.s3.connection import OrdinaryCallingFormat, S3Connection
import boto3
import botocore 
import boto


def create_new_user(name): 
    s3 = boto3.resource('s3', region_name = 'us-west-2') 
                            

        
        

        