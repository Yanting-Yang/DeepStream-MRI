source .venv/bin/activate
export FLASK_ENV=development
export FLASK_APP=flaskr
# export FLASK_RUN_PORT=80
export FLASK_RUN_PORT=5000
export FLASK_RUN_HOST=0.0.0.0
flask run
