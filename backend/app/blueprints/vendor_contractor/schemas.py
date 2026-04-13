from app.extensions import ma
from app.models.role import Role


class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        load_instance = True


role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)