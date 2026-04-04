from flask import Flask
from sqlalchemy import text
import time

from app.extensions import db, ma
from app.config import Config
from app.logging_config import setup_logging


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    setup_logging()

    db.init_app(app)
    ma.init_app(app)

    from app.blueprints.vendor_users.model import VendorUser
    from app.blueprints.user.model import User
    from app.blueprints.address.model import Address
    from app.blueprints.vendor.model import Vendor

    with app.app_context():
        for i in range(10):
            try:
                db.session.execute(text("SELECT 1"))
                print("Database is ready")
                break
            except Exception as e:
                print(f"Database not ready yet, retrying... ({i + 1}/10): {e}")
                time.sleep(2)
        else:
            raise RuntimeError("Database was not ready after multiple attempts")

        db.create_all()

    from app.blueprints.user.controller.routes import user_bp
    from app.blueprints.address.controller.routes import address_bp
    from app.blueprints.vendor.controller.routes import vendor_bp
    from app.blueprints.vendor.controller.registration_routes import (
        vendor_registration_bp,
    )
    from app.blueprints.vendor_users.controller.routes import vendor_user_bp

    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(address_bp, url_prefix="/addresses")
    app.register_blueprint(vendor_bp, url_prefix="/vendors")
    app.register_blueprint(vendor_registration_bp, url_prefix="/vendors")
    app.register_blueprint(vendor_user_bp, url_prefix="/vendor_users")

    return app
