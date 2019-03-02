from flask import Flask
from gesture_api.config import Config


def create_app(app_name):
    app = Flask(app_name)

    app.config.from_object(Config)

    from gesture_api.apiv1 import apiv1
    app.register_blueprint(apiv1, url_prefix='/')

    return app
