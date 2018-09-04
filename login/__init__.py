from flask import Flask
from login.ext import init_ext


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'abcxyz'
    init_ext(app)
    return app