from . import routes
from flask import render_template
# a simple page that says hello
@routes.route('/')
def hello():
    return render_template('index.html')

