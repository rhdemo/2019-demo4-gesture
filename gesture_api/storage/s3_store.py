import json
import os

import boto3
from time import gmtime, strftime


class S3Store:
    def __init__(self, prefix: str = '', *, host: str = None, key_id: str = None,
                 secret_key: str = None, bucket: str = None, region: str = None):
        super().__init__()
        self.host = host
        self.key_id = key_id
        self.secret_key = secret_key
        self.bucket = bucket
        self.region = region
        self.prefix = prefix
        self._s3 = None
        self.connect()

    def connect(self) -> None:
        self._s3 = boto3.resource('s3',
                                  endpoint_url=os.environ.get('S3_ENDPOINT'),
                                  aws_access_key_id=os.environ.get('S3_ACCESS_KEY_ID'),
                                  aws_secret_access_key=os.environ.get('S3_SECRET_ACCESS_KEY'),
                                  region_name=os.environ.get('S3_REGION'))

        for bucket in self._s3.buckets.all():
            print(bucket.name)

    def write_dict(self, data: dict, object_key: str) -> dict:
        serialized_data = json.dumps(data, sort_keys=True, separators=(',', ': '), indent=2).encode()
        key = os.path.join(self.prefix, object_key)
        response = self._s3.Bucket(self.bucket).put_object(Key=key, Body=serialized_data)
        return response
