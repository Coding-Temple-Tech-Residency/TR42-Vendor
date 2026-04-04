from app.extensions import ma

from app.blueprints.address.model import Address


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address
        load_instance = True
        include_fk = True


address_schema = AddressSchema()
addresses_schema = AddressSchema(many=True)
