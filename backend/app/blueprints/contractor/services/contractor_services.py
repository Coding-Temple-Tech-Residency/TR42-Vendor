from marshmallow import ValidationError
import logging

from sqlalchemy.exc import IntegrityError
from app.extensions import db
from app.blueprints.contractor.repositories.contractor_repositories import (
    ContractorRepository,
)
from app.blueprints.user.repositories.user_repositories import UserRepository
from app.blueprints.vendor_contractor.repositories.vendor_contractor_repositories import (
    VendorContractorRepository,
)
from app.blueprints.user.model import User, UserType
from app.blueprints.contractor.model import Contractor
from app.blueprints.contractor.schemas import (
    contractor_schema,
)
from app.blueprints.vendor_contractor.model import (
    VendorContractor,
    VendorContractorRole,
)
from app.functions import generate_uuid


logger = logging.getLogger(__name__)


class ContractorService:

    @staticmethod
    def get_all_contractors():
        return ContractorRepository.get_all()

    @staticmethod
    def get_contractor(contractor_id):
        return ContractorRepository.get_by_id(contractor_id)

    @staticmethod
    def create_contractor(
        validated_data: dict, vendor_id: str, vendor_manager_id: str | None
    ):
        try:
            logger.info("Creating a contractor in the service layer")

            if UserRepository.get_by_email(validated_data["email"]):
                raise ValidationError({"email": ["User email already exists."]})

            if UserRepository.get_by_username(validated_data["username"]):
                raise ValidationError({"username": ["Username already exists."]})

            user = User(
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
                email=validated_data["email"],
                username=validated_data["username"],
                user_type=UserType.CONTRACTOR,
                is_active=True,
                is_admin=False,
                profile_photo=validated_data["profile_photo"],
                created_by=vendor_manager_id,
                updated_by=vendor_manager_id,
            )
            user.set_password(validated_data["password"])
            UserRepository.create(user)
            db.session.flush()

            employee_seed = generate_uuid()

            contractor = Contractor(
                user_id=user.id,
                employee_number=f"EMP-{employee_seed[:8].upper()}",
                vendor_manager_id=vendor_manager_id,
                status=validated_data["status"],
                tickets_completed=validated_data["tickets_completed"],
                tickets_open=validated_data["tickets_open"],
                biometric_enrolled=validated_data["biometric_enrolled"],
                is_onboarded=validated_data["is_onboarded"],
                is_subcontractor=validated_data["is_subcontractor"],
                is_fte=validated_data["is_fte"],
                is_licensed=validated_data["is_licensed"],
                is_insured=validated_data["is_insured"],
                is_certified=validated_data["is_certified"],
                average_rating=validated_data["average_rating"],
                years_experience=validated_data["years_experience"],
                created_by=vendor_manager_id,
                updated_by=vendor_manager_id,
            )

            ContractorRepository.create(contractor)
            db.session.flush()

            vendor_contractor = VendorContractor(
                vendor_id=vendor_id,
                contractor_id=contractor.id,
                vendor_contractor_role=validated_data["vendor_contractor_role"],
                created_by=vendor_manager_id,
                updated_by=vendor_manager_id,
            )

            VendorContractorRepository.create(vendor_contractor)
            db.session.commit()
            return contractor

        except ValidationError:
            db.session.rollback()
            raise

        except IntegrityError:
            db.session.rollback()
            raise ValueError("Contractor creation failed due to a database constraint")

        except Exception:
            db.session.rollback()
            logger.exception("Failed to create contractor in service layer")
            raise

    @staticmethod
    def update_contractor(contractor_id: str, contractor_data: dict):
        try:
            existing_contractor = ContractorRepository.get_by_id(contractor_id)
            if not existing_contractor:
                logger.warning("Contractor with id not found for update")
                return None

            validated_data = contractor_schema.load(contractor_data, partial=True)
            logger.debug("Contractor data validated successfully")

            for key, value in validated_data.items():
                setattr(existing_contractor, key, value)

            db.session.commit()
            db.session.refresh(existing_contractor)
            return existing_contractor

        except ValidationError:
            db.session.rollback()
            raise

        except Exception:
            db.session.rollback()
            logger.exception("Failed to update contractor in service layer")
            raise

    @staticmethod
    def delete_contractor(contractor):
        ContractorRepository.delete(contractor)
        return True
