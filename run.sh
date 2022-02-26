#!/bin/bash
source .venv/bin/activate;
export FLASK_APP=flaskr;
export FLASK_RUN_PORT=5000;
export FLASK_RUN_HOST=0.0.0.0;

case "$1" in
    "debug")
        export FLASK_ENV=development;
        flask run;;
    "deploy")
        export FLASK_ENV=production;
        nohup flask run >./logs/$(date "+%Y-%m-%d").log 2>&1 &;;
    "kill")
        str=$(netstat -tunlp 2>/dev/null);
        pid=$(echo "$str"|grep ":5000"|grep -Po '[0-9]+(?=\/python)');
        echo "kill $pid"
        kill $pid;;
    "init")
        python -m venv .venv;
        source .venv/bin/activate;
        pip install --upgrade pip;
        pip install -r requirements.txt;;
esac