from flask import Flask
from app.extensions import db, ma
from app.config import Config
from app.logging_config import setup_logging
# from work_order import register_work_order
# from ticket import register_ticket
# from contractor import register_contractor


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    setup_logging()

    db.init_app(app)
    ma.init_app(app)

     # Import models so SQLAlchemy knows them
    # IMPORTANT: Order matters because of relationships
    from app.blueprints.user.model import User
    from app.blueprints.vendor_users.model import VendorUser
    from app.blueprints.address.model import Address
    from app.blueprints.vendor.model import Vendor

    # try:
    #     from app.blueprints.vendor_users import register_vendor_user

    #     app.register_blueprint(register_vendor_user, url_prefix="/vendor_user")
    # except ImportError:
    #     pass

    # try:
    #     from app.blueprints.vendors import register_vendors

    #     app.register_blueprint(register_vendors)
    # except ImportError as e:
    #     print(f"Vendor blueprint import failed: {e}")

    # try:
    #     from app.blueprints.work_order import register_work_order

    #     app.register_blueprint(register_work_order)
    # except ImportError as e:
    #     print(f"Work order blueprint import failed: {e}")

    # try:
    #     from app.blueprints.ticket import register_ticket

    #     app.register_blueprint(register_ticket)
    # except ImportError as e:
    #     print(f"Ticket blueprint import failed: {e}")

    # try:
    #     from app.blueprints.contractor import register_contractor

    #     app.register_blueprint(register_contractor)
    # except ImportError as e:
    #     print(f"Contractor blueprint import failed: {e}")


 # Now that all models are registered, create tables
    with app.app_context():
        db.create_all()

    # from app.blueprints.vendor import routes as routes
    # from app.blueprints.address import routes as routes
    # from app.blueprints.user import routes as routes
    # from app.blueprints.vendor_users import routes as routes


    


    # Register blueprints AFTER models are imported
    #from app.blueprints.auth.routes import auth_bp
    from app.blueprints.user.routes import user_bp
    from app.blueprints.address.routes import address_bp
    from app.blueprints.vendor.routes import vendor_bp
    from app.blueprints.vendor.registration_routes import vendor_registration_bp
    from app.blueprints.vendor_users.routes import vendor_user_bp
    

    #app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(address_bp, url_prefix="/addresses")
    app.register_blueprint(vendor_bp, url_prefix="/vendors")
    app.register_blueprint(vendor_registration_bp, url_prefix="/vendors")
    app.register_blueprint(vendor_user_bp, url_prefix="/vendor_users")

   

    return app
