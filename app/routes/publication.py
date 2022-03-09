from . import routes
from flask import render_template

@routes.route('/publication')
def publication():
    return render_template('publication.html')

