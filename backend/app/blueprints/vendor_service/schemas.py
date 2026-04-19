from app.blueprints.vendor_service.model import VendorService
from app.extensions import ma

class VendorServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VendorService
        load_instance = True
        include_fk = True

vendor_service_schema = VendorServiceSchema()
vendor_services_schema = VendorServiceSchema(many=True)
