from app.extensions import db
from app.blueprints.services.model import Service

class ServiceRepository:

    @staticmethod
    def create(service: Service):
        db.session.add(service)
        db.session.commit()
        return service

    @staticmethod
    def get_all():
        return Service.query.all()

    @staticmethod
    def get_by_id(service_id: str):
        return Service.query.get(service_id)

    @staticmethod
    def update(service: Service):
        db.session.commit()
        return service

    @staticmethod
    def delete(service: Service):
        db.session.delete(service)
        db.session.commit()
        return True
