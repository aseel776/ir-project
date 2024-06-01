from core.endpoints import HOME
from flask import Blueprint, render_template

blueprint = Blueprint('home', __name__)

@blueprint.route(HOME)
def home():
    return render_template("home.html")