from app.extensions import db
from app.blueprints.user.model import User
from app.blueprints.vendor.model import Vendor
from app.blueprints.address.model import Address
from app.blueprints.vendor_users.model import VendorUser
from app.blueprints.user.utils import hash_password
import uuid

class VendorRegistrationService:

    @staticmethod
    def register(data):

        user_data = data["user"]
        vendor_data = data["vendor"]
        address_data = data["address"]

        try:
            with db.session.begin():

                # 1. Create Address
                address = Address(
                    address_id=str(uuid.uuid4()),
                    street=address_data["street"],
                    city=address_data["city"],
                    state=address_data["state"],
                    zipcode=address_data["zipcode"],
                    country="US",
                    created_by="system",
                    updated_by="system"
                    
                )
                db.session.add(address)

                # 2. Create Vendor (mapped to your existing Vendor model)
                vendor = Vendor(
                    vendor_id=str(uuid.uuid4()),
                    company_name=vendor_data["company_name"],
                    company_code=vendor_data["service_type"],  # mapped
                    primary_contact_name=f"{user_data['first_name']} {user_data['last_name']}",
                    company_email=vendor_data["company_email"],
                    company_phone=vendor_data["company_phone"],
                    status="active",
                    onboarding=True,
                    compliance_status="incomplete",
                    address_id=address.address_id,
                    
                )
                db.session.add(vendor)

                # 3. Create User (Vendor Admin)
                user = User(
                    user_id=str(uuid.uuid4()),
                    first_name=user_data["first_name"],
                    last_name=user_data["last_name"],
                    email=user_data["email"],
                    username=user_data["username"],
                    password=hash_password(user_data["password"]),
                    type="vendor",
                    is_admin=True,
                    created_by="system",
                    updated_by="system"
                )
                db.session.add(user)

                # 4. Link Vendor ↔ User
                link = VendorUser(
                    id=str(uuid.uuid4()),
                    vendor_id=vendor.vendor_id,
                    user_id=user.user_id,
                    role="admin",
                    created_by="system",
                    updated_by="system"
                )
                db.session.add(link)

            return {
                "message": "Vendor account created successfully",
                "vendor_id": vendor.vendor_id,
                "user_id": user.user_id,
                "address_id": address.address_id
            }

        except Exception as e:
            db.session.rollback()
            raise e
