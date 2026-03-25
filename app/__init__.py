from flask import Flask
from .extensions import db, ma
from .config import Config
from app.blueprints.address import address_bp 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(address_bp, url_prefix="/address") 

    return app
