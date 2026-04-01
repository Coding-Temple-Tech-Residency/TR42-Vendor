from flask import Flask
from app.extensions import db, ma
from app.config import Config
from app.logging_config import setup_logging
from work_order import register_work_order
from ticket import register_ticket
from contractor import register_contractor


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    setup_logging()

    db.init_app(app)
    ma.init_app(app)

    try:
        from app.blueprints.vendor_users import register_vendor_user

        app.register_blueprint(register_vendor_user, url_prefix="/vendor_user")
    except ImportError:
        pass

    try:
        from app.blueprints.vendors import register_vendors

        app.register_blueprint(register_vendors)
    except ImportError as e:
        print(f"Vendor blueprint import failed: {e}")

    try:
        from app.blueprints.work_order import register_work_order

        app.register_blueprint(register_work_order)
    except ImportError as e:
        print(f"Work order blueprint import failed: {e}")

    try:
        from app.blueprints.ticket import register_ticket

        app.register_blueprint(register_ticket)
    except ImportError as e:
        print(f"Ticket blueprint import failed: {e}")

    try:
        from app.blueprints.contractor import register_contractor

        app.register_blueprint(register_contractor)
    except ImportError as e:
        print(f"Contractor blueprint import failed: {e}")

    with app.app_context():
        db.create_all()

    return app
