from app.extensions import db
from app.blueprints.address.model import Address
from app.blueprints.address.repositories.address_repositories import AddressRepository


def test_create_saves_address(app):
    address = Address(
        street="123 Main St",
        city="Denver",
        state="CO",
        zipcode="80202",
        country="USA",
        created_by_user_id="user-1",
        updated_by_user_id="user-1",
    )

    result = AddressRepository.create(address)
    db.session.commit()

    assert result is not None
    assert result.address_id is not None
    assert result.street == "123 Main St"
