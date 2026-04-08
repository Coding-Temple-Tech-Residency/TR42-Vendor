from marshmallow import ValidationError, fields, pre_load, validates, validates_schema
from app.extensions import ma
from app.functions import (
    strip_input,
    validate_email_format,
    validate_name,
    validate_password,
    validate_phone_format,
)


class UserRegistrationSchema(ma.Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True, load_only=True)
    # confirm_password = fields.String(required=True, load_only=True)

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
        if not value or not value.strip():
            raise ValidationError("Username is required.")

    @validates("password")
    def check_password(self, value, **kwargs):
        return validate_password(value, min_length=6)

    # @validates_schema
    # def validate_password_match(self, data, **kwargs):
    #     if data.get("password") != data.get("confirm_password"):
    #         raise ValidationError({"confirm_password": ["Passwords do not match."]})


user_registration_schema = UserRegistrationSchema()


class VendorRegistrationSchema(ma.Schema):
    company_name = fields.String(required=True)
    address = fields.String(required=True)
    city = fields.String(required=True)
    state = fields.String(required=True)
    zipcode = fields.String(required=True)
    company_email = fields.Email(required=True)
    company_phone = fields.String(required=True)
    primary_contact_name = fields.String(required=True)
    service_type = fields.String(required=True)

    @pre_load
    def preprocess(self, data, **kwargs):
        return strip_input(data)

    @validates("company_name")
    def validate_company_name(self, value, **kwargs):
        return validate_name(value, field_name="Company name")

    @validates("primary_contact_name")
    def validate_primary_contact_name(self, value, **kwargs):
        return validate_name(value, field_name="Primary contact name")

    @validates("company_email")
    def validate_company_email(self, value, **kwargs):
        return validate_email_format(value)

    @validates("company_phone")
    def validate_company_phone(self, value, **kwargs):
        return validate_phone_format(value)

    @validates("address")
    def validate_address(self, value, **kwargs):
        if not value or not value.strip():
            raise ValidationError("Address is required.")

    @validates("city")
    def validate_city(self, value, **kwargs):
        if not value or not value.strip():
            raise ValidationError("City is required.")

    @validates("state")
    def validate_state(self, value, **kwargs):
        if not value or not value.strip():
            raise ValidationError("State is required.")

    @validates("zipcode")
    def validate_zipcode(self, value, **kwargs):
        if not value or not value.strip():
            raise ValidationError("Zip code is required.")

    @validates("service_type")
    def validate_service_type(self, value, **kwargs):
        if not value or not value.strip():
            raise ValidationError("Select a service type.")


class CombinedRegistrationSchema(ma.Schema):
    user = fields.Nested(UserRegistrationSchema, required=True)
    vendor = fields.Nested(VendorRegistrationSchema, required=True)


user_registration_schema = UserRegistrationSchema()
vendor_registration_schema = VendorRegistrationSchema()
combined_registration_schema = CombinedRegistrationSchema()
