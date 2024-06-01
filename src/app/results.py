from flask import Blueprint, render_template

blueprint = Blueprint('results', __name__)

@blueprint.route('/results')
def results():
    return render_template("results.html")