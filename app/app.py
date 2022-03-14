from flask import Flask
from .routes import *

# 'flask run' automatically detects an app (app or application) or factory (create_app or make_app).
# create and configure the app
App = Flask(__name__)
App.register_blueprint(Route)