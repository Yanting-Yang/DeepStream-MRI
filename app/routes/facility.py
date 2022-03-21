from .route import Route
from flask import render_template

@Route.route('/facility')
def Facility():
    return render_template('facility.html')