#!/bin/bash
echo 'Starting to Deploy...'

ssh yangyanting@18.188.192.202 "
    cd DeepStream-MRI/
    bash run.sh kill
    git pull
    bash run.sh deploy
    "

echo 'Deployment completed successfully'