from .route import Route
from flask import render_template

@Route.route('/info')
def Info():
    return render_template('info.html')