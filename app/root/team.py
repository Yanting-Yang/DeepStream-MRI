from .blueprint import root
from flask import render_template

@root.route('/team')
def team():
    return render_template('team.html')
