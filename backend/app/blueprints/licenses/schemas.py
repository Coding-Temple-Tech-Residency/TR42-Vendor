from app.extensions import ma
from app.blueprints.licenses.model import License


class LicenseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = License
        load_instance = True

    
    
    
license_schema = LicenseSchema()
licenses_schema = LicenseSchema(many=True)