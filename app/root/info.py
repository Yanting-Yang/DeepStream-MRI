from .blueprint import root
from flask import render_template

@root.route('/info')
def info():
    return render_template('info.html')