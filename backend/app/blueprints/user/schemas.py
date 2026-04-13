from app.extensions import ma
from marshmallow import fields, pre_load, validates, validate
from app.blueprints.user.model import User
from app.functions import (
    strip_input,
    validate_name,
    validate_email_format,
    validate_password,
)


class UserSchema(ma.SQLAlchemyAutoSchema):  
    # Below is the user_type field I added to the UserSchema. I got a TypeError: object of type 'UserType' has no len() when running creating user test. I think it might be because I am trying to validate the user_type field as a string but it is an enum in the database. I will need to change the validation to check if the value is one of the enum values instead of checking if it is a string.^^
    user_type = fields.String(
        required=True,
        validate= validate.OneOf(["operator", "vendor", "contractor"])
    ) # ^^
    
    password = fields.String(required=True, load_only=True)

    vendor_links = fields.Nested(
        "VendorUserSchema",
        many=True,
        dump_only=True,
        exclude=("user",),
    )

    class Meta:
        model = User
        load_instance = False
        include_fk = True
        exclude = ("password_hash",)

    @pre_load
    def preprocess(self, data, **kwargs):
        return strip_input(data)

    @validates("first_name")
    def check_first_name(self, value, **kwargs):
        return validate_name(value, field_name="First name")

    @validates("last_name")
    def check_last_name(self, value, **kwargs):
        return validate_name(value, field_name="Last name")

    @validates("email")
    def check_email(self, value, **kwargs):
        return validate_email_format(value)

    @validates("username")
    def check_username(self, value, **kwargs):
        return validate_name(value, field_name="Username")

    @validates("password")
    def check_password(self, value, **kwargs):
        return validate_password(value, min_length=6)

    #vendor_links = fields.Nested("VendorUserSchema", many=True, dump_only=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
