from app.extensions import db
from ..model import Vendor
from app.blueprints.address.model import Address
from werkzeug.exceptions import BadRequest


class VendorRepository:

    @staticmethod
    def get_all():
        return Vendor.query.all()

    @staticmethod
    def get_by_id(vendor_id: str):
        return Vendor.query.get(vendor_id)

    @staticmethod
    def create_vendor(data: dict):
        try:
            # Extract nested address
            #address_data = data.pop("address")

            # # Check vendor_id duplicate
            # vendor_id = data["vendor_id"]
            # if Vendor.query.get(vendor_id):
            #     return {"error": f"Vendor with ID {vendor_id} already exists"}, 400

            # Check company_name duplicate
            if Vendor.query.filter_by(company_name=data["company_name"]).first():
                raise BadRequest("Company name already exists")

            # ALWAYS create a new address
            # address = Address(**address_data)
            # db.session.add(address)

            # Create vendor and link address
            # vendor = Vendor(**data, address=address)
            # db.session.add(vendor)
            vendor = Vendor(**data)
            db.session.add(vendor)

            db.session.commit()
            
            return vendor

        except Exception as e:
            db.session.rollback()
            raise e

    