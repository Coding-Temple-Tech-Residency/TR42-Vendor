from app.extensions import ma
from app.blueprints.services.model import Service

class ServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Service
        load_instance = True
        include_fk = True

service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)
