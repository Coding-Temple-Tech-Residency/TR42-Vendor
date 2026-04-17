from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from .model import Role


class RoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        include_fk = True
        load_instance = True


role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)
