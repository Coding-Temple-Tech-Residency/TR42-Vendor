from flask import Flask
from sqlalchemy import text
import time

from app.extensions import db, ma
from app.config import Config
from app.logging_config import setup_logging



def create_app(config_object=None):
    app = Flask(__name__)

    if config_object:
        app.config.from_object(config_object)
    else:
        app.config.from_object(Config)

    setup_logging()

    db.init_app(app)
    ma.init_app(app)

    from app.blueprints.user.model import User
    from app.blueprints.address.model import Address
    from app.blueprints.vendor.model import Vendor
    from app.blueprints.vendor_user.model import VendorUser
    from app.blueprints.background_check.model import BackgroundCheck
    from app.blueprints.drug_test.model import DrugTest
    from app.blueprints.contractors.model import Contractor
    from app.blueprints.contractor_performance.model import ContractorPerformance
    from app.blueprints.ticket.model import Ticket
    from app.blueprints.well.model import Well
    from app.blueprints.work_orders.model import WorkOrder
    from app.blueprints.licenses.model import License
    #from app.blueprints.registration.model import Registration
    from app.blueprints.certifications.model import Certification
    #from app.blueprints.communication.model import Communication
    #from app.blueprints.finance.model import LineItem
    #from app.blueprints.fraud_alerts.model import FraudAlert
    from app.blueprints.insurance.model import Insurance
    from app.blueprints.invoice.model import Invoice
    #from app.blueprints.msa.model import MSA
    #from app.blueprints.role.model import Role
    #from app.blueprints.services.model import Service
    from app.blueprints.system.model import Session, Notification
    #from app.blueprints.ticket_extras.model import TicketPhoto
    
    
    
    
    

    with app.app_context():
        if not app.config.get("TESTING"):
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
        
    from app.blueprints.user.controller.user_routes import user_bp
    from app.blueprints.address.controller.address_routes import address_bp
    from app.blueprints.vendor.controller.vendor_routes import vendor_bp
    #from app.blueprints.registration.controller.registration_routes import registration_bp
    from app.blueprints.vendor_user.controller.vendor_user_routes import vendor_user_bp
    from app.blueprints.contractor_performance.controller.contractor_performance_routes import contractor_performance_bp
    from app.blueprints.contractors.controller.contractors_routes import contractor_bp
    from app.blueprints.ticket.controller.ticket_routes import ticket_bp
    from app.blueprints.work_orders.controller.routes import work_order_bp
    from app.blueprints.background_check.controller.background_check_routes import background_check_bp
    from app.blueprints.drug_test.controller.drug_test_routes import drug_test_bp
    from app.blueprints.licenses.controller.routes import license_bp
    from app.blueprints.certifications.controller.certifications_routes import certification_bp
    #from app.blueprints.communication.controller.routes import communication_bp
    #from app.blueprints.finance.controller.routes import line_item_bp
    #from app.blueprints.fraud_alerts.controller.routes import fraud_alert_bp
    from app.blueprints.insurance.controller.routes import insurance_bp
    from app.blueprints.invoice.controller.routes import invoice_bp
    #from app.blueprints.msa.controller.routes import msa_bp
    #from app.blueprints.role.controller.routes import Role
    #from app.blueprints.services.controller.routes import service_bp
    from app.blueprints.system.controller.system_routes import session_bp, notification_bp
    #from app.blueprints.ticket_extras.controller.routes import ticket_photo
    from app.blueprints.well.controller.routes import well_bp
    
    



    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(address_bp, url_prefix="/api/addresses")
    app.register_blueprint(vendor_bp, url_prefix="/api/vendors")
    #app.register_blueprint(registration_bp, url_prefix="/api/registration")
    app.register_blueprint(vendor_user_bp, url_prefix="/api/vendor_users")
    app.register_blueprint(contractor_performance_bp, url_prefix="/api/contractor_performance")
    app.register_blueprint(contractor_bp, url_prefix="/api/contractors")
    app.register_blueprint(ticket_bp, url_prefix="/api/tickets")
    app.register_blueprint(work_order_bp, url_prefix="/api/work_orders")
    app.register_blueprint(background_check_bp, url_prefix="/api/background_check")
    app.register_blueprint(drug_test_bp, url_prefix="/api/drug_tests")
    app.register_blueprint(license_bp, url_prefix="/api/licenses")
    app.register_blueprint(certification_bp, url_prefix="/api/certifications")
    #app.register_blueprint(communication_bp, url_prefix="/api/communication")
    #app.register_blueprint(line_item_bp, url_prefix="/api/line_items")
    #app.register_blueprint(fraud_alert_bp, url_prefix="/api/fraud_alerts")
    app.register_blueprint(insurance_bp, url_prefix="/api/insurance")
    app.register_blueprint(invoice_bp, url_prefix="/api/invoices")
    #app.register_blueprint(msa_bp, url_prefix="/api/msa")
    #app.register_blueprint(role_bp, url_prefix="/api/roles")
    #app.register_blueprint(service_bp, url_prefix="/api/services")
    app.register_blueprint(session_bp, url_prefix="/api/sessions")
    app.register_blueprint(notification_bp, url_prefix="/api/notifications")
    #app.register_blueprint(ticket_photo_bp, url_prefix="/api/ticket_photos")
    app.register_blueprint(well_bp, url_prefix="/api/wells")
    return app