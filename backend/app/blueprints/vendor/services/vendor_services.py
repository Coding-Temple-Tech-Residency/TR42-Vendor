from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from app.blueprints.vendor.repositories.vendor_repositories import VendorRepository
from app.blueprints.vendor.model import Vendor
from app.blueprints.address.model import Address
from app.blueprints.address.repositories.address_repositories import (
    AddressRepository,
)
from app.functions import generate_uuid

from app.extensions import db
import logging


logger = logging.getLogger(__name__)


class VendorService:

    @staticmethod
    def get_all_vendors():
        try:
            logger.debug("Retrieving all vendors from service layer")
            return VendorRepository.get_all()
        except Exception:
            logger.exception("Failed to retrieve vendors in service layer")
            raise

    @staticmethod
    def create_vendor(validated_data: dict, user_id: str):
        try:
            logger.info("Creating vendor in service layer")

            if VendorRepository.get_by_company_name(validated_data["company_name"]):
                raise ValidationError(
                    {"vendor": {"company_name": ["Company name already exists."]}}
                )
            if VendorRepository.get_by_company_email(validated_data["company_email"]):
                raise ValidationError(
                    {"vendor": {"company_email": ["Company email already exists."]}}
                )
            if VendorRepository.get_by_company_name(validated_data["company_name"]):
                raise ValidationError(
                    {"vendor": {"company_name": ["Company name already exists."]}}
                )

            address = Address(
                street=validated_data["street"],
                city=validated_data["city"],
                state=validated_data["state"],
                zipcode=validated_data["zipcode"],
                created_by_user_id=user_id,
                updated_by_user_id=user_id,
            )
            AddressRepository.create(address)
            db.session.flush()

            vendor_id = generate_uuid()

            vendor = Vendor(
                vendor_id=vendor_id,
                company_name=validated_data["company_name"],
                company_email=validated_data["company_email"],
                company_phone=validated_data["company_phone"],
                primary_contact_name=validated_data["primary_contact_name"],
                service_type=validated_data["service_type"],
                vendor_code=f"Vendor-{vendor_id[:8].upper()}",
                address_id=address.address_id,
                created_by_user_id=user_id,
                updated_by_user_id=user_id,
            )
            VendorRepository.create(vendor)
            db.session.flush()

            db.session.commit()
            return vendor

        except IntegrityError:
            db.session.rollback()
            raise ValueError("Vendor creation failed due to a database constraint")

        except Exception:
            db.session.rollback()
            logger.exception("Failed to create vendor in service layer")
            raise

    @staticmethod
    def get_vendor_by_id(vendor_id: str):
        try:
            logger.info("Getting vendor by id")
            vendor = VendorRepository.get_by_id(vendor_id)
            return vendor
        except Exception:
            logger.exception("Failed to retrieve vendor in service layer")
            raise

    @staticmethod
    def update_vendor(vendor_id: int, data: Vendor): ...

    @staticmethod
    def delete_vendor(vendor_id: int): ...
