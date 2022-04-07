#!/bin/bash
echo 'Starting to Deploy...'

ssh yangyanting@18.188.192.202 "
    cd DeepStream-MRI/
    bash run.sh kill
    git fetch
    git reset --hard HEAD
    git merge origin/main
    bash run.sh init
    bash run.sh deploy
    "

echo 'Deployment completed successfully'