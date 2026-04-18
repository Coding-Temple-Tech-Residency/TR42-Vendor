from app.extensions import db
from app.blueprints.vendor_service.model import VendorService

class VendorServiceRepository:

    @staticmethod
    def create(vendor_service: VendorService):
        db.session.add(vendor_service)
        db.session.commit()
        return vendor_service
    
    @staticmethod
    def get_all():
        return VendorService.query.all()

    @staticmethod
    def get_by_vendor(vendor_id: str):
        return VendorService.query.filter_by(vendor_id=vendor_id).all()

    @staticmethod
    def get_by_id(id: str):
        return VendorService.query.get(id)

    @staticmethod
    def update(vendor_service: VendorService):
        db.session.commit()
        return vendor_service

    @staticmethod
    def delete(vendor_service: VendorService):
        db.session.delete(vendor_service)
        db.session.commit()
        return True
