from .blueprint import root
from flask import render_template

@root.route('/')
def index():
    return render_template('index.html')

