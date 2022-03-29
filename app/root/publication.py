from .blueprint import root
from flask import render_template

@root.route('/publication')
def publication():
    return render_template('publication.html')