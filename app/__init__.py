from flask import Flask
from .extensions import db, ma
from .config import Config
from app.auth import vendor_auth_bp 
from app.blueprints.vendor_user import vendor_user_bp
from app.blueprints.vendor_role import vendor_role_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    
    app.register_blueprint(vendor_auth_bp, url_prefix="/vendor")
    app.register_blueprint(vendor_user_bp, url_prefix="/vendor_user")
    app.register_blueprint(vendor_role_bp, url_prefix="/vendor_role")
    return app
