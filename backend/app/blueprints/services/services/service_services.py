from app.blueprints.services.repositories.service_repositories import ServiceRepository
from app.blueprints.services.schemas import service_schema
from app.blueprints.services.model import Service
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest


class ServiceService:

    @staticmethod
    def create(data):
        try:
            
            service = service_schema.load(data)
            return ServiceRepository.create(service)
        except ValidationError as e:
            raise BadRequest(e.messages)
    
    @staticmethod
    def get_all():
        return ServiceRepository.get_all()



    @staticmethod
    def get(service_id: str):
        return ServiceRepository.get_by_id(service_id)

    @staticmethod
    def update(service: Service, data):
        try:
            # Load into the existing instance
            updated_service = service_schema.load(data, instance=service, partial=True)
            return ServiceRepository.update(updated_service)
        except ValidationError as e:
            raise BadRequest(e.messages)


    @staticmethod
    def delete(service: Service):
        return ServiceRepository.delete(service)
