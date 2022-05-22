#!/bin/bash
app="deepstream-mri"
username="yangyanting"
docker build -t ${username}/${app} .
docker run -d -p 127.0.0.1:5000:5000 --name=${app} ${username}/${app}
