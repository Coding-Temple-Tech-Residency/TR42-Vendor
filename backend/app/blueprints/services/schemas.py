from app.extensions import ma
from app.models.services import Service


class ServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Service
        load_instance = True


service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)