import os

from flask import Flask

# 'flask run' automatically detects an app (app or application) or factory (create_app or make_app).
def create_app():
    # create and configure the app
    app = Flask(__name__)
    
    from .routes import routes
    app.register_blueprint(routes)

    return app
