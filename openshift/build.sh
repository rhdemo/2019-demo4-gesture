#!/usr/bin/env bash
#set -x

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

[[ -z "${IMAGE_REPOSITORY}" ]] && { IMAGE_REPOSITORY="quay.io/redhatdemo/demo4-gesture:latest"; }
[[ -z "${GIT_REPOSITORY}" ]] && { GIT_REPOSITORY="git@github.com:rhdemo/2019-demo4-gesture.git"; }
[[ -z "${GIT_BRANCH}" ]] && { GIT_BRANCH="master"; }

echo "Building ${IMAGE_REPOSITORY} from ${GIT_REPOSITORY} on ${GIT_BRANCH}"

s2i build ${GIT_REPOSITORY} --ref ${GIT_BRANCH} docker.io/centos/python-36-centos7:latest ${IMAGE_REPOSITORY}



