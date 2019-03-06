#!/usr/bin/env bash
#set -x

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

[[ -f "${DIR}/../.secrets" ]] && source "${DIR}/../.secrets"

SECRET_NAME=demo4-scm-key
SECRET=$(oc get secret ${SECRET_NAME} 2>/dev/null)

if [[ -z "$SECRET" ]]
then
  echo "${SECRET_NAME} missing.  Creating..."
  [[ -z "${SCM_SSH_KEY_PATH}" ]] && { SCM_SSH_KEY_PATH="${HOME}/.ssh/id_rsa"; }
  oc create secret generic ${SECRET_NAME} --from-file=ssh-privatekey=${SCM_SSH_KEY_PATH} --type=kubernetes.io/ssh-auth
else
  echo "${SECRET_NAME} found"
fi

oc process -f "${DIR}/full-build.yml" \
  -p S3_ENDPOINT=${S3_ENDPOINT} \
  -p S3_REGION=${S3_REGION} \
  -p S3_BUCKET=${S3_BUCKET} \
  -p S3_PREFIX=${S3_PREFIX} \
  -p S3_ACCESS_KEY_ID=${S3_ACCESS_KEY_ID} \
  -p S3_SECRET_ACCESS_KEY=${S3_SECRET_ACCESS_KEY} \
  -p SECRET_KEY=${SECRET_KEY} \
  | oc create -f -
