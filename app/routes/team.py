from .route import Route
from flask import render_template

@Route.route('/team')
def Team():
    return render_template('team.html')
