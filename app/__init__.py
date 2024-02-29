from flask import Flask
from .routes import routes
from .services import link_services
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app) # This will enable CORS for all routes

    # Register the blueprint
    app.register_blueprint(routes.bp)

    return app
   
