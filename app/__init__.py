"""

application creation

"""
from flask import Flask

from instance.config import app_config


def create_app(config):
    """function configuring the Flask App"""
    app = Flask(__name__)

    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config])
    app.config["TESTING"] = True

    return app

