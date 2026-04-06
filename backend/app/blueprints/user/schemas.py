from app.extensions import ma
# from marshmallow import fields
from app.blueprints.user.model import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True

    #vendor_links = fields.Nested("VendorUserSchema", many=True, dump_only=True)



user_schema = UserSchema()
users_schema = UserSchema(many=True)