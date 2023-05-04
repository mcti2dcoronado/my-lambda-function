import boto3
import os

from botocore.exceptions import NoCredentialsError

def lambda_handler(event, context):
    return None

def upload_to_aws(local_file, s3_file):
    s3 = boto3.client('s3')
 
    try:
        s3.upload_file(local_file, os.environ['my-bucket-mtl'], s3_file)
        url = s3.generate_presigned_url(
            ClientMethod = 'get_object',
            Params={
                'Bucket': os.environ['my-bucket-mtl'],
                'Key': s3_file
            },
            ExpiresIn=24 * 3600
        )

        print("Upload Successful", url)
        return url
    except FileNotFoundError:
        print("The file was not found")
        return None
    except NoCredentialsError:
        print("Credentials not available")
        return None
