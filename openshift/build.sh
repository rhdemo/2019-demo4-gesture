#!/usr/bin/env bash
#set -x

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

[[ -f "${DIR}/../.secrets" ]] && source "${DIR}/../.secrets"

[[ -z "${IMAGE_REPOSITORY}" ]] && { IMAGE_REPOSITORY="quay.io/redhatdemo/demo4-gesture:latest"; }

echo "Building ${IMAGE_REPOSITORY}"

s2i build git@github.com:rhdemo/2019-demo4-gesture.git docker.io/centos/python-36-centos7:latest ${IMAGE_REPOSITORY}
docker push ${IMAGE_REPOSITORY}



