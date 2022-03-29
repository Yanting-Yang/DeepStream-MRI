from flask import Flask, render_template
from .root import root
# 'flask run' automatically detects an app (app or application) or factory (create_app or make_app).
# create and configure the app

app = Flask(__name__)
app.register_blueprint(root)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404