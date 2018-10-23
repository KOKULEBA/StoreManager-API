""" Application creation """
from flask import Flask

from instance.config import app_config
from app.views.authentication import authentication
from app.views.products import product
from app.views.sales import sale


def create_app(config):
    """ Function configuring the Flask App """
    app = Flask(__name__)

    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config])
    app.config["TESTING"] = True

    app.register_blueprint(authentication)
    app.register_blueprint(product)
    app.register_blueprint(sale)

    return app
