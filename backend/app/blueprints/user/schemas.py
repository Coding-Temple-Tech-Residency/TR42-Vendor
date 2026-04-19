from marshmallow import ValidationError, fields, pre_load, validates
from app.extensions import ma
from app.functions import (
    strip_input,
    validate_name,
    validate_email_format,
    validate_password,
    validate_phone_format,
)
from app.blueprints.address.schemas import AddressSchema
from app.blueprints.user.model import User


class UserCreateSchema(ma.Schema):
    first_name = fields.String(required=True)
    middle_name = fields.String(load_default=None)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True, load_only=True)

    contact_number = fields.String(required=True)
    alternate_number = fields.String(load_default=None)
    date_of_birth = fields.Date(load_default=None)
    ssn_last_four = fields.String(load_default=None)

    user_type = fields.String(required=True)
    profile_photo = fields.Raw(load_default=None)

    address = fields.Nested(AddressSchema, required=True)

    @pre_load
    def preprocess(self, data, **kwargs):
        return strip_input(data)

    @validates("first_name")
    def check_first_name(self, value, **kwargs):
        validate_name(value, field_name="First name")

    @validates("last_name")
    def check_last_name(self, value, **kwargs):
        validate_name(value, field_name="Last name")

    @validates("email")
    def check_email(self, value, **kwargs):
        validate_email_format(value)

    @validates("username")
    def check_username(self, value, **kwargs):
        if not value or not value.strip():
            raise ValidationError("Username is required.")

    @validates("password")
    def check_password(self, value, **kwargs):
        validate_password(value)

    @validates("contact_number")
    def check_contact_number(self, value, **kwargs):
        validate_phone_format(value)

    @validates("alternate_number")
    def check_alternate_number(self, value, **kwargs):
        if value:
            validate_phone_format(value)

    @validates("ssn_last_four")
    def check_ssn_last_four(self, value, **kwargs):
        if value and (not value.isdigit() or len(value) != 4):
            raise ValidationError("SSN last four must be exactly 4 digits.")


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = False
        include_fk = True
        exclude = ("password_hash",)


user_create_schema = UserCreateSchema()
user_schema = UserSchema()
users_schema = UserSchema(many=True)
