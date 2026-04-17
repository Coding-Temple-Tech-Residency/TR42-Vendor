from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from app.blueprints.vendor.repositories.vendor_repositories import VendorRepository
from app.blueprints.vendor.model import Vendor
from app.blueprints.address.model import Address
from app.blueprints.address.repositories.address_repositories import (
    AddressRepository,
)
from app.blueprints.vendor.schemas import vendor_schema, vendors_schema
from app.functions import generate_uuid
from app.extensions import db
import logging

from app.blueprints.vendor_user.model import VendorUser, VendorUserRole
from app.blueprints.vendor_user.repositories.vendor_user_repositories import (
    VendorUserRepository,
)


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
    def get_all_paginated(page: int = 1, per_page: int = 10):
        pagination = VendorRepository.get_all_paginated(page=page, per_page=per_page)

        return {
            "total": pagination.total,
            "page": pagination.page,
            "pages": pagination.pages,
            "per_page": pagination.per_page,
            "vendors": vendors_schema.dump(pagination.items),
        }

    @staticmethod
    def create_vendor(validated_data: dict, id: str):
        try:
            logger.info("Creating vendor in service layer")

            if VendorRepository.get_by_company_name(validated_data["company_name"]):
                raise ValidationError(
                    {"company_name": ["Company name already exists."]}
                )
            if VendorRepository.get_by_company_email(validated_data["company_email"]):
                raise ValidationError(
                    {"company_email": ["Company email already exists."]}
                )

            address_data = validated_data["address"]

            address = Address(
                street=address_data["street"],
                city=address_data["city"],
                state=address_data["state"],
                zip=address_data["zip"],
                created_by=id,
                updated_by=id,
            )
            AddressRepository.create(address)
            db.session.flush()

            vendor_id = generate_uuid()

            vendor = Vendor(
                id=vendor_id,
                company_name=validated_data["company_name"],
                company_email=validated_data["company_email"],
                company_phone=validated_data["company_phone"],
                primary_contact_name=validated_data["primary_contact_name"],
                service_type=validated_data["service_type"],
                vendor_code=f"Vendor-{vendor_id[:8].upper()}",
                address_id=address.id,
                created_by=id,
                updated_by=id,
            )
            VendorRepository.create(vendor)
            db.session.flush()

            vendor_user = VendorUser(
                vendor_id=vendor.id,
                user_id=id,
                vendor_user_role=VendorUserRole.ADMIN,
                created_by=id,
                updated_by=id,
            )
            VendorUserRepository.create(vendor_user)
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
    def update_vendor(vendor_id: str, vendor_data: dict):
        try:
            existing_vendor = VendorRepository.get_by_id(vendor_id)
            if not existing_vendor:
                logger.warning(f"Vendor with id not found for update")
                return None

            validated_data = vendor_schema.load(vendor_data, partial=True)
            logger.debug(f"Vendor data validated successfully for vendor id")

            address_data = validated_data.pop("address", None)

            for key, value in validated_data.items():
                setattr(existing_vendor, key, value)

            if address_data is not None:
                if existing_vendor.address:
                    for key, value in address_data.items():
                        setattr(existing_vendor.address, key, value)
                else:
                    new_address = Address(**address_data)
                    db.session.add(new_address)
                    db.session.flush()
                    existing_vendor.address = new_address

            db.session.commit()
            db.session.refresh(existing_vendor)
            return existing_vendor

        except Exception:
            db.session.rollback()
            logger.exception("Failed to update vendor in service layer")
            raise

    @staticmethod
    def delete_vendor(vendor_id: str):
        try:
            existing_vendor = VendorService.get_vendor_by_id(vendor_id)
            if not existing_vendor:
                logger.warning("Vendor with id not found for deletion")
                return None

            VendorRepository.delete(existing_vendor)
            db.session.commit()
            return True
        except Exception:
            logger.exception("Failed to delete vendor in service layer")
            raise
