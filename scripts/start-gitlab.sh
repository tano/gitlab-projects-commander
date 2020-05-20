#!/bin/bash

# GITLAB_HOME should be set up.
if [[ -z "$GITLAB_HOME" ]];
then
  echo "Please set GITLAB_HOME environment variable."
  exit 1
fi

docker run --detach \
  --hostname gitlab.example.com \
  --publish 443:443 --publish 80:80 --publish 22:22 \
  --name gitlab \
  --restart always \
  --volume $GITLAB_HOME/gitlab/config:/etc/gitlab \
  --volume $GITLAB_HOME/gitlab/logs:/var/log/gitlab \
  --volume $GITLAB_HOME/gitlab/data:/var/opt/gitlab \
  gitlab/gitlab-ce:latest
