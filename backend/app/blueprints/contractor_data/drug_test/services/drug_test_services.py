import logging
from marshmallow import ValidationError

from app.extensions import db
from app.blueprints.contractor.repositories.contractor_repositories import (
    ContractorRepository,
)
from app.blueprints.contractor_data.drug_test.model import DrugTest
from app.blueprints.contractor_data.drug_test.repositories.drug_test_repositories import (
    DrugTestRepository,
)

logger = logging.getLogger(__name__)


class DrugTestService:

    @staticmethod
    def create_drug_test(
        contractor_id: str,
        validated_data: dict,
        created_by: str | None,
        updated_by: str | None,
    ):
        try:
            logger.debug("Creating drug test")

            contractor = ContractorRepository.get_by_id(contractor_id)
            if not contractor:
                raise ValidationError({"contractor_id": ["Contractor not found."]})

            drug_test = DrugTest(
                contractor_id=contractor_id,
                drug_test_passed=validated_data["drug_test_passed"],
                drug_test_date=validated_data.get("drug_test_date"),
                created_by=created_by,
                updated_by=updated_by,
            )

            DrugTestRepository.create(drug_test)

            db.session.commit()
            db.session.refresh(drug_test)

            logger.info("Drug test created successfully")
            return drug_test

        except ValidationError:
            db.session.rollback()
            raise
        except Exception:
            db.session.rollback()
            logger.exception("Failed to create drug test")
            raise

    @staticmethod
    def get_drug_tests_by_contractor(contractor_id: str):
        try:
            logger.debug("Fetching drug tests by contractor_id")

            contractor = ContractorRepository.get_by_id(contractor_id)
            if not contractor:
                raise ValidationError({"contractor_id": ["Contractor not found."]})

            return DrugTestRepository.get_by_contractor(contractor_id)

        except ValidationError:
            raise
        except Exception:
            logger.exception("Failed to fetch drug tests by contractor_id")
            raise

    @staticmethod
    def get_drug_test(drug_test_id: str):
        try:
            logger.debug("Fetching drug test by id")

            drug_test = DrugTestRepository.get_by_id(drug_test_id)
            if not drug_test:
                return None

            return drug_test

        except Exception:
            logger.exception("Failed to fetch drug test by id")
            raise

    @staticmethod
    def update_drug_test(
        drug_test_id: str,
        validated_data: dict,
        updated_by: str | None,
    ):
        try:
            logger.debug("Updating drug test")

            drug_test = DrugTestRepository.get_by_id(drug_test_id)
            if not drug_test:
                return None

            if "drug_test_passed" in validated_data:
                drug_test.drug_test_passed = validated_data["drug_test_passed"]

            if "drug_test_date" in validated_data:
                drug_test.drug_test_date = validated_data.get("drug_test_date")

            drug_test.updated_by = updated_by

            DrugTestRepository.update(drug_test)

            db.session.commit()
            db.session.refresh(drug_test)

            logger.info("Drug test updated successfully")
            return drug_test

        except ValidationError:
            db.session.rollback()
            raise
        except Exception:
            db.session.rollback()
            logger.exception("Failed to update drug test")
            raise

    @staticmethod
    def delete_drug_test(drug_test_id: str):
        try:
            logger.debug("Deleting drug test")

            drug_test = DrugTestRepository.get_by_id(drug_test_id)
            if not drug_test:
                return None

            DrugTestRepository.delete(drug_test)
            db.session.commit()

            logger.info("Drug test deleted successfully")
            return True

        except Exception:
            db.session.rollback()
            logger.exception("Failed to delete drug test")
            raise
