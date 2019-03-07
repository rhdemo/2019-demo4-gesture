import os
from flask import Blueprint
from gesture_api.storage import S3Store, MockStore

prefix = os.environ.get('S3_PREFIX')
host = os.environ.get('S3_ENDPOINT')
key_id = os.environ.get('S3_ACCESS_KEY_ID')
secret_key = os.environ.get('S3_SECRET_ACCESS_KEY')
bucket = os.environ.get('S3_BUCKET')
region = os.environ.get('S3_REGION')

if prefix and host and key_id and secret_key and bucket and region:
    print('storage enabled to:')
    print(f'Endpoint: {host}')
    print(f'Region: {region}')
    print(f'Bucket: {bucket}')
    storage = S3Store(prefix, host=host, key_id=key_id, secret_key=secret_key, bucket=bucket, region=region)
else:
    print('Storage disabled.  Using MockStore.')
    storage = MockStore()

apiv1 = Blueprint('apiv1', __name__)

from gesture_api.apiv1 import errors, status, gesture

