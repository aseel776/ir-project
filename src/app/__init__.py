import os
from app import home
from app import results
from flask import Flask

def createApp():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)

    app.register_blueprint(home.blueprint)
    app.register_blueprint(results.blueprint)

    return app