source .venv/bin/activate
export FLASK_ENV=development
export FLASK_APP=flaskr
export FLASK_RUN_PORT=5000
export FLASK_RUN_HOST=0.0.0.0
nohup flask run >/dev/null 2>error.log &