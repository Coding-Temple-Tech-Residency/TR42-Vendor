from app.extensions import db
from app.blueprints.role.model import Role


class RoleRepository:

    @staticmethod
    def get_all():
        return Role.query.all()

    @staticmethod
    def get_by_id(role_id: str):
        return Role.query.get(role_id)

    @staticmethod
    def create(role: Role):
        db.session.add(role)
        db.session.commit()
        return role

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(role: Role):
        db.session.delete(role)
        db.session.commit()
