from .route import Route
from flask import render_template

@Route.route('/facility')
def Facility():
    return render_template('facility.html')

@Route.route('/facility/wet-lab-equipments')
def Wet_Lab_Equipments():
    return render_template('wet-lab-equipments.html')

@Route.route('/facility/computing-facilities')
def Computing_Facilities():
    return render_template('computing-facilities.html')

@Route.route('/facility/bruker-biospec-94-30')
def Bruker_Biospec_94_30():
    return render_template('bruker-biospec-94-30.html')

@Route.route('/facility/physiological-monitoring-devices')
def Physiological_Monitoring_Devices():
    return render_template('physiological-monitoring-devices.html')