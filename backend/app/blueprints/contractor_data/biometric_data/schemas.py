from marshmallow import Schema, fields
from app.extensions import ma
from app.blueprints.contractor_data.biometric_data.model import BiometricData


class BiometricDataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BiometricData
        load_instance = False
        include_fk = True
        include_relationships = False


class BiometricDataCreateSchema(Schema):
    biometric_enrollment_data = fields.String(required=False, allow_none=True)


biometric_data_schema = BiometricDataSchema()
biometric_data_list_schema = BiometricDataSchema(many=True)
biometric_data_create_schema = BiometricDataCreateSchema()
