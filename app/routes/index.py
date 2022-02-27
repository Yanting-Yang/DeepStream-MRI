from . import routes
from flask import render_template

@routes.route('/')
def hello():
    return render_template('index.html')

