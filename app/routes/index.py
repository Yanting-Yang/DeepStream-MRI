from .route import Route
from flask import render_template

@Route.route('/')
def Index():
    return render_template('index.html')

