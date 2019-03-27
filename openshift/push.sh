#!/usr/bin/env bash
#set -x

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

[[ -z "${IMAGE_REPOSITORY}" ]] && { IMAGE_REPOSITORY="quay.io/redhatdemo/demo4-gesture:latest"; }

echo "Pushing ${IMAGE_REPOSITORY}"

docker push ${IMAGE_REPOSITORY}



