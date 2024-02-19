from flask import Flask
from .routes import routes


def create_app():
    app = Flask(__name__)

    # Register the blueprint
    app.register_blueprint(routes.bp)

    return app
