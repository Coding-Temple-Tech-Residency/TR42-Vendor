from flask import Flask
from sqlalchemy import text
import time
from flask_cors import CORS

from app.extensions import db, ma
from app.config import Config
from app.logging_config import setup_logging


def create_app(config_object=None):
    app = Flask(__name__)
    CORS(
        app,
        resources={r"/*": {"origins": "http://localhost:5173"}},
    )

    if config_object:
        app.config.from_object(config_object)
    else:
        app.config.from_object(Config)

    setup_logging()

    db.init_app(app)
    ma.init_app(app)

    # Import all models BEFORE blueprints to ensure they're registered with SQLAlchemy
    from app import models

    with app.app_context():
        if not app.config.get("TESTING"):

            for i in range(10):
                try:
                    db.session.execute(text("SELECT 1"))
                    print("Database is ready")
                    break
                except Exception as e:
                    print(f"Database not ready yet, retrying... ({i + 1}/api/10): {e}")
                    time.sleep(2)
            else:
                raise RuntimeError("Database was not ready after multiple attempts")

        db.create_all()

        # Now import blueprints
    from app.blueprints.user.controller.user_routes import user_bp
    from app.blueprints.address.controller.address_routes import address_bp
    from app.blueprints.vendor.controller.vendor_routes import vendor_bp
    from app.blueprints.registration.controller.registration_routes import (
        registration_bp,
    )
    from app.blueprints.vendor_user.controller.vendor_user_routes import vendor_user_bp
    from app.blueprints.work_orders.controller.work_order_routes import work_order_bp
    from app.blueprints.invoices.controller.invoice_routes import invoice_bp
    from app.blueprints.invoices.controller.lineitem_routes import lineItem_bp

    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(address_bp, url_prefix="/api/addresses")
    app.register_blueprint(vendor_bp, url_prefix="/api/vendors")
    app.register_blueprint(registration_bp, url_prefix="/api/registration")
    app.register_blueprint(vendor_user_bp, url_prefix="/api/vendor_users")
    app.register_blueprint(work_order_bp, url_prefix="/api/work_orders")
    app.register_blueprint(invoice_bp, url_prefix="/api/invoices")
    app.register_blueprint(lineItem_bp, url_prefix="/api/line_items")

    return app
