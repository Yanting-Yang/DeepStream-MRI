from flask import redirect, render_template
import pandas as pd
from . import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/info')
def info():
    return render_template('info.html')

@main.route('/team')
def team():
    path = 'app/static/members.csv'
    df = pd.read_csv(path)
    df.fillna('',inplace=True)
    data = df.to_dict(orient='index')
    return render_template('team.html', data=data)

@main.route('/publication')
def publication():
    return render_template('publication.html')

@main.route('/facility/', defaults={'page': 'index'})
@main.route('/facility/<page>')
def facility(page):
    if page in ['index', 'bruker-biospec-94-30', 'computing-facilities', 'physiological-monitoring-devices', 'wet-lab-equipments']:
        return render_template(f'facility/{page}.html')
    return render_template('404.html'), 404