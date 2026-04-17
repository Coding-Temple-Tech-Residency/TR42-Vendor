from app.blueprints.role.repositories.role_repositories import RoleRepository
from app.blueprints.role.schemas import role_schema, roles_schema
from app.blueprints.vendor_user.model import VendorUserRole


class RoleService:

    @staticmethod
    def get_all():
        roles = RoleRepository.get_all()
        return roles_schema.dump(roles)

    @staticmethod
    def get_by_id(role_id: str):
        role = RoleRepository.get_by_id(role_id)
        return role_schema.dump(role) if role else None

    @staticmethod
    def create(data: dict):
        role = role_schema.load(data)
        saved = RoleRepository.create(role)
        return role_schema.dump(saved)

    @staticmethod
    def update(role_id: str, data: dict):
        role = RoleRepository.get_by_id(role_id)
        if not role:
            return None

        for key, value in data.items():
            setattr(role, key, value)

        RoleRepository.update()
        return role_schema.dump(role)

    @staticmethod
    def delete(role_id: str):
        role = RoleRepository.get_by_id(role_id)
        if not role:
            return None

        RoleRepository.delete(role)
        return True
