import os

from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    CORS(app)

    from src.api import api
    api.init_app(app)

    return app
