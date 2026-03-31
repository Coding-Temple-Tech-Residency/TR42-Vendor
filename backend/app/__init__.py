from flask import Flask
from app.extensions import db, ma
from app.config import Config
from app.logging_config import setup_logging


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    setup_logging()

    db.init_app(app)
    ma.init_app(app)

    try:
        from app.blueprints.vendor_users import vendor_users_bp

        app.register_blueprint(vendor_users_bp, url_prefix="/vendor_user")
    except ImportError:
        pass

    try:
        from app.blueprints.vendors import vendors_bp

        app.register_blueprint(vendors_bp)
    except ImportError as e:
        print(f"Vendor blueprint import failed: {e}")

    with app.app_context():
        db.create_all()

    return app
