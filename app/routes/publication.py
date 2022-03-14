from .route import Route
from flask import render_template

@Route.route('/publication')
def Publication():
    return render_template('publication.html')

