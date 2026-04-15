from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from app.extensions import db
from app.blueprints.registration.schemas import combined_registration_schema
from app.blueprints.user.model import User, UserType
from app.blueprints.user.repositories.user_repositories import UserRepository
from app.blueprints.vendor.model import Vendor
from app.blueprints.vendor.repositories.vendor_repositories import (
    VendorRepository,
)
from app.blueprints.address.model import Address
from app.blueprints.address.repositories.address_repositories import (
    AddressRepository,
)
from app.blueprints.vendor_user.model import VendorUser, VendorUserRole
from app.blueprints.vendor_user.repositories.vendor_user_repositories import (
    VendorUserRepository,
)

from logging import getLogger


logger = getLogger(__name__)


class RegistrationService:

    @staticmethod
    def register_vendor_account(payload):
        data = combined_registration_schema.load(payload)

        user_data = data["user"]
        vendor_data = data["vendor"]

        if UserRepository.get_by_email(user_data["email"]):
            raise ValidationError({"user": {"email": ["Email already in use."]}})

        if UserRepository.get_by_username(user_data["username"]):
            raise ValidationError({"user": {"username": ["Username already in use."]}})

        if VendorRepository.get_by_company_name(vendor_data["company_name"]):
            raise ValidationError(
                {"vendor": {"company_name": ["Company name already exists."]}}
            )

        try:
            user = User(
                first_name=user_data["first_name"],
                last_name=user_data["last_name"],
                email=user_data["email"],
                username=user_data["username"],
                user_type=UserType.VENDOR,
                is_active=True,
                is_admin=True,
                
            )
            user.set_password(user_data["password"])
            UserRepository.create(user)
            db.session.flush()

            address = Address(
                street=vendor_data["address"],
                city=vendor_data["city"],
                state=vendor_data["state"],
                zipcode=vendor_data["zipcode"],
                created_by_user_id=user.id,
                updated_by_user_id=user.id,
            )
            AddressRepository.create(address)
            db.session.flush()

            vendor = Vendor(
                company_name=vendor_data["company_name"],
                company_email=vendor_data["company_email"],
                company_phone=vendor_data["company_phone"],
                primary_contact_name=vendor_data["primary_contact_name"],
                service_type=vendor_data["service_type"],
                address_id=address.id,
                created_by_user_id=user.id,
                updated_by_user_id=user.id,
            )
            VendorRepository.create(vendor)
            db.session.flush()

            vendor_user = VendorUser(
                vendor_id=vendor.id,
                user_id=user.id,
                vendor_user_role=VendorUserRole.ADMIN,
                created_by_user_id=user.id,
                updated_by_user_id=user.id,
            )
            VendorUserRepository.create(vendor_user)
            db.session.flush()

            db.session.commit()

        except IntegrityError as e:
            db.session.rollback()
            logger.exception("IntegrityError during vendor registration: %s", e)
            raise ValidationError(
                {
                    "error": [
                        f"Registration failed due to a database constraint: {e.orig}"
                    ]
                }
            )

        except Exception as e:
            db.session.rollback()
            logger.exception("Unexpected error during vendor registration: %s", e)
            raise

        return {
            "message": "Registration successful.",
            "user_id": user.id,
            "vendor_id": vendor.id,
            "address_id": address.id,
        }
