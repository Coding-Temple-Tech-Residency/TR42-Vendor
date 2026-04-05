from app.extensions import db
from app.blueprints.vendor.model import Vendor
from app.blueprints.address.model import Address
from app.blueprints.user.model import User
from app.blueprints.vendor_users.model import VendorUser
import uuid

class VendorRegistrationRepository:

    @staticmethod
    def create_address(data):
        address = Address(
            address_id=str(uuid.uuid4()),
            street=data["street"],
            city=data["city"],
            state=data["state"],
            zipcode=data["zipcode"],
            country="US",
            created_by="system",
            updated_by="system"
        )
        db.session.add(address)
        return address

    @staticmethod
    def create_vendor(data, address_id, user_full_name):
        vendor = Vendor(
            vendor_id=str(uuid.uuid4()),
            company_name=data["company_name"],
            company_code=data["service_type"],
            primary_contact_name=user_full_name,
            contact_email=data["company_email"],
            contact_phone=data["company_phone"],
            status="active",
            onboarding=True,
            compliance_status="incomplete",
            address_id=address_id,
            created_by="system",
            updated_by="system"
        )
        db.session.add(vendor)
        return vendor

    @staticmethod
    def create_user(data):
        user = User(
            user_id=str(uuid.uuid4()),
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            username=data["username"],
            password=data["password"],  # already hashed
            type="vendor",
            is_admin=True,
            created_by="system",
            updated_by="system"
        )
        db.session.add(user)
        return user

    @staticmethod
    def create_vendor_user_link(user_id, vendor_id):
        link = VendorUser(
            id=str(uuid.uuid4()),
            vendor_id=vendor_id,
            user_id=user_id,
            role="admin",
            created_by="system",
            updated_by="system"
        )
        db.session.add(link)
        return link
