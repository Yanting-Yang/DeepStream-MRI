#!/bin/bash
app="deepstream-mri"
username="yangyanting"

case "$1" in
    "build_run")
        docker build -t ${username}/${app} .
        docker run -d -p 127.0.0.1:5000:5000 --name=${app} ${username}/${app}
        ;;
    "pull_run")
        docker pull ${username}/${app}
        docker stop ${app}
        docker rm ${app}
        docker run --init -d -p 127.0.0.1:5000:5000 --name=${app} ${username}/${app}
        ;;
esac


