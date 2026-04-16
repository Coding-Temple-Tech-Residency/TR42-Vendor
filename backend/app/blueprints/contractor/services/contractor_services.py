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
    contractors_schema,
)
from app.blueprints.vendor_contractor.model import (
    VendorContractor,
    VendorContractorRole,
)
from app.blueprints.address.model import Address
from app.functions import generate_uuid
from app.blueprints.address.repositories.address_repositories import AddressRepository
from app.blueprints.contractor.repositories.contractor_invite_repositories import (
    ContractorInviteRepository,
)


logger = logging.getLogger(__name__)


class ContractorService:

    @staticmethod
    def get_all_vendor_contractors_paginated(
        vendor_id: str,
        page: int = 1,
        per_page: int = 10,
    ):
        pagination = ContractorRepository.get_by_vendor_paginated(
            vendor_id=vendor_id,
            page=page,
            per_page=per_page,
        )

        return {
            "total": pagination.total,
            "page": pagination.page,
            "pages": pagination.pages,
            "per_page": pagination.per_page,
            "contractors": contractors_schema.dump(pagination.items),
        }

    @staticmethod
    def get_contractor(contractor_id):
        return ContractorRepository.get_by_id(contractor_id)

    @staticmethod
    def create_contractor_by_manager(
        validated_data: dict, vendor_id: str, vendor_manager_id: str
    ):
        try:
            contractor = ContractorService._create_contractor_records(
                validated_data=validated_data,
                vendor_id=vendor_id,
                vendor_manager_id=vendor_manager_id,
                created_by=vendor_manager_id,
                updated_by=vendor_manager_id,
            )
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
            logger.exception("Failed to create contractor by manager")
            raise

    @staticmethod
    def self_register_contractor(validated_data, invite_token):
        try:
            invite = ContractorInviteRepository.get_valid_by_token(invite_token)

            if not invite:
                raise ValidationError(
                    {"invite_token": ["Invalid or expired invite token."]}
                )

            if validated_data["email"].lower() != invite.email.lower():
                raise ValidationError({"email": ["This invite is not for this email."]})

            contractor = ContractorService._create_contractor_records(
                validated_data=validated_data,
                vendor_id=invite.vendor_id,
                vendor_manager_id=getattr(invite, "vendor_manager_id", None),
                created_by=None,
                updated_by=None,
            )

            invite.is_used = True
            db.session.commit()

            return contractor

        except ValidationError:
            db.session.rollback()
            raise

        except IntegrityError:
            db.session.rollback()
            raise ValueError(
                "Contractor self-registration failed due to a database constraint"
            )

        except Exception:
            db.session.rollback()
            logger.exception("Failed to self-register contractor")
            raise

    @staticmethod
    def _create_contractor_records(
        validated_data,
        vendor_id,
        vendor_manager_id,
        created_by,
        updated_by,
    ):
        try:
            logger.info("Creating contractor records")

            if UserRepository.get_by_email(validated_data["email"]):
                raise ValidationError({"email": ["User email already exists."]})

            if UserRepository.get_by_username(validated_data["username"]):
                raise ValidationError({"username": ["Username already exists."]})

            address_data = validated_data["address"]
            contractor_address = Address(
                street=address_data["street"],
                city=address_data["city"],
                state=address_data["state"],
                zip=address_data["zip"],
                created_by=created_by,
                updated_by=updated_by,
            )
            AddressRepository.create(contractor_address)
            db.session.flush()

            user = User(
                first_name=validated_data["first_name"],
                middle_name=validated_data.get("middle_name"),
                last_name=validated_data["last_name"],
                email=validated_data["email"],
                username=validated_data["username"],
                contact_number=validated_data["contact_number"],
                alternate_number=validated_data.get("alternate_number"),
                date_of_birth=validated_data.get("date_of_birth"),
                ssn_last_four=validated_data.get("ssn_last_four"),
                address_id=contractor_address.id,
                user_type=UserType.CONTRACTOR,
                is_active=True,
                is_admin=False,
                profile_photo=validated_data.get("profile_photo"),
                created_by=created_by,
                updated_by=updated_by,
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
                created_by=created_by,
                updated_by=updated_by,
            )
            ContractorRepository.create(contractor)
            db.session.flush()

            vendor_contractor = VendorContractor(
                vendor_id=vendor_id,
                contractor_id=contractor.id,
                vendor_contractor_role=validated_data["vendor_contractor_role"],
                created_by=created_by,
                updated_by=updated_by,
            )
            VendorContractorRepository.create(vendor_contractor)
            db.session.flush()

            return contractor

        except ValidationError:
            db.session.rollback()
            raise

        except IntegrityError:
            db.session.rollback()
            raise ValueError("Contractor creation failed due to a database constraint")

        except Exception:
            db.session.rollback()
            logger.exception("Failed to create contractor records")
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
