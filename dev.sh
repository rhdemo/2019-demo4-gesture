#!/bin/bash

#set -x

source .secrets

export S3_ACCESS_KEY_ID=$S3_ACCESS_KEY_ID
export S3_SECRET_ACCESS_KEY=$S3_SECRET_ACCESS_KEY
export S3_ENDPOINT=$S3_ENDPOINT
export S3_REGION=$S3_REGION
export S3_BUCKET=$S3_BUCKET
export S3_PREFIX=$S3_PREFIX

export SECRET_KEY="LocalRun"
export SERVER_PORT=8084
export FLASK_DEBUG=true

source venv/bin/activate

FILE_NAME="${1:-wsgi.py}"

if [ "$FILE_NAME" == "shell" ]; then
  python
else
  python ${FILE_NAME}
fi