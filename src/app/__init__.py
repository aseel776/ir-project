from app import home
from core.endpoints import HOME
from flask import Flask

def createApp():
    app = Flask(__name__)

    app.register_blueprint(home.blueprint, url_prefix = HOME)

    return app  