from flask import Flask
from .extensions import db, ma
from .config import Config
from app.blueprints.vendor_user import vendor_user_bp
from .logging_config import setup_logging


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    setup_logging() 

    db.init_app(app)
    ma.init_app(app)

    
    
    app.register_blueprint(vendor_user_bp, url_prefix="/vendor_user")
    
    return app
