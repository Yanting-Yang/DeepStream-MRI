from .blueprint import root
from flask import render_template
import pandas as pd

@root.route('/team')
def team():
    path = 'app/static/members.csv'
    df = pd.read_csv(path)
    df.fillna('',inplace=True)
    data = df.to_dict(orient='index')
    return render_template('team.html', data=data)
