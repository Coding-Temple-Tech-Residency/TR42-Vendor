from app.blueprints.vendor.repositories.vendors_repository import VendorRepository
from werkzeug.exceptions import BadRequest


class VendorService:
   

    @staticmethod
    def create(data):
        try:
            vendor = VendorRepository.create_vendor(data)
            return vendor
        except Exception as e:
            raise BadRequest(str(e))

    @staticmethod
    def get_all():
        return VendorRepository.get_all()

    @staticmethod
    def get(vendor_id):
        return VendorRepository.get_by_id(vendor_id)

    @staticmethod
    def update(vendor_id, data):
        vendor = VendorRepository.get_by_id(vendor_id)
        if not vendor:
            return None
        return VendorRepository.update(vendor, data)

    @staticmethod
    def delete(vendor_id):
        vendor = VendorRepository.get_by_id(vendor_id)
        if not vendor:
            return None
        return VendorRepository.delete(vendor)