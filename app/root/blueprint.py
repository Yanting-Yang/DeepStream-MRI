from flask import Blueprint
from .facility import facility

root = Blueprint('root', __name__)
root.register_blueprint(facility)