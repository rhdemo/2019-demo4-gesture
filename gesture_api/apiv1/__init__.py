import os
from flask import Blueprint
from gesture_api.storage import S3Store

storage = S3Store(
    os.environ.get('S3_PREFIX'),
    host=os.environ.get('S3_ENDPOINT'),
    key_id=os.environ.get('S3_ACCESS_KEY_ID'),
    secret_key=os.environ.get('S3_SECRET_ACCESS_KEY'),
    bucket=os.environ.get('S3_BUCKET'),
    region=os.environ.get('S3_REGION')
)

apiv1 = Blueprint('apiv1', __name__)

from gesture_api.apiv1 import errors, status, gesture

