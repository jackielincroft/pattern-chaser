from flask import Flask
from flask_bootstrap import Bootstrap
from .pattern_class import Pattern

def create_app(configfile=None):
    app = Flask(__name__, template_folder = 'templates')
    bootstrap = Bootstrap(app)
    return app