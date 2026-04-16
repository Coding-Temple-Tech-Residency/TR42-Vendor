from app.extensions import ma
from marshmallow import fields, pre_load, validates, validates_schema
from app.blueprints.contractor.model import ContractorStatus
from app.functions import (
    strip_input,
    validate_name,
    validate_email_format,
    validate_password,
    validate_password_content,
)
from app.extensions import ma
from marshmallow import fields
from app.blueprints.contractor.model import Contractor
from app.blueprints.vendor_contractor.model import VendorContractorRole


class ContractorCreateSchema(ma.Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True, load_only=True)
    profile_photo = fields.String(allow_none=True, required=False)

    vendor_contractor_role = fields.Enum(
        VendorContractorRole,
        by_value=True,
        load_default=VendorContractorRole.WORKER,
    )

    status = fields.Enum(
        ContractorStatus,
        by_value=True,
        load_default=ContractorStatus.ACTIVE,
    )

    tickets_completed = fields.Integer(load_default=0)
    tickets_open = fields.Integer(load_default=0)

    biometric_enrolled = fields.Boolean(load_default=False)
    is_onboarded = fields.Boolean(load_default=False)
    is_subcontractor = fields.Boolean(load_default=False)
    is_fte = fields.Boolean(load_default=False)
    is_licensed = fields.Boolean(load_default=False)
    is_insured = fields.Boolean(load_default=False)
    is_certified = fields.Boolean(load_default=False)

    average_rating = fields.Float(load_default=0.0)
    years_experience = fields.Integer(allow_none=True, load_default=None)

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
        validate_name(value, field_name="Username")

    @validates("password")
    def check_password(self, value, **kwargs):
        validate_password(value)

    @validates_schema
    def check_password_content(self, data, **kwargs):
        validate_password_content(data)


class ContractorSchema(ma.SQLAlchemyAutoSchema):
    status = fields.Enum(ContractorStatus, by_value=True)

    class Meta:
        model = Contractor
        load_instance = False
        include_fk = True
        include_relationships = False


contractor_create_schema = ContractorCreateSchema()
contractor_schema = ContractorSchema()
contractors_schema = ContractorSchema(many=True)
