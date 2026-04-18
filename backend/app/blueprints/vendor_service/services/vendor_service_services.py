from app.blueprints.vendor_service.repositories.vendor_service_repositories import VendorServiceRepository
from app.blueprints.vendor_service.schemas import vendor_service_schema
from app.blueprints.vendor_service.model import VendorService
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest
from app.extensions import db

class VendorServiceService:

    @staticmethod
    def create(data):
        try:
            vs = vendor_service_schema.load(data)   # already a VendorService instance
            return VendorServiceRepository.create(vs)

        except ValidationError as e:
            raise BadRequest(e.messages)
        except Exception as e:
            db.session.rollback()
            print("REAL ERROR:", e)
            raise BadRequest(str(e))


    @staticmethod
    def get_all():
        return VendorServiceRepository.get_all()

    @staticmethod
    def get(id: str):
        return VendorServiceRepository.get_by_id(id)

    @staticmethod
    def get_by_vendor(vendor_id: str):
        return VendorServiceRepository.get_by_vendor(vendor_id)

    @staticmethod
    def update(vendor_service, data):
        updated = vendor_service_schema.load(
            data,
            instance=vendor_service,
            partial=True
        )
        return VendorServiceRepository.update(updated)

    @staticmethod
    def delete(vendor_service):
        return VendorServiceRepository.delete(vendor_service)