from flask_bootstrap import Bootstrap
from login.views import blue

def init_ext(app):
    app.register_blueprint(blueprint=blue)
    Bootstrap(app)