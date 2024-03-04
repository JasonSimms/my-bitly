from flask import Flask, jsonify
from .routes import routes
import logging
import traceback

# from .services import link_services
from flask_cors import CORS
from .routes.user_routes import user_bp
from .routes.user_link_routes import user_link_bp
from .routes import routes


def create_app():
    app = Flask(__name__)
    CORS(app)  # This will enable CORS for all routes

    # Register the blueprint
    app.register_blueprint(routes.bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(user_link_bp)

    return app
