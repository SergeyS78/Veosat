"""Flask instance fabric.

    for start application:
        flask run
"""

from flask import Flask
# flask_restplus is dead now, move to flask-restx. Or downgrading to Werkzeug==0.16.1 to solves this
# from flask_restplus import Api
from app.rest_x import api
from config import Config
from app.database import db
import app.veosat.routes as veosat
import app.veosat_rest_x.routes as veosat_rest_x



def create_app(config_class=Config):
    """Function to create Flask instance"""

    app = Flask(__name__)

    # applying applications config
    app.config.from_object(config_class)

    # data base initialization
    db.init_app(app)
    # flask_restx initialization
    api.init_app(app)

    # application module register in application instance
    app.register_blueprint(veosat.module)
    # app.register_blueprint(veosat_rest_x.module)

    @app.route('/')
    @app.route('/index')
    def index():
        return 'Hello, World'

    return app
