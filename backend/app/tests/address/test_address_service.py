from unittest.mock import patch
import pytest

from sqlalchemy.exc import IntegrityError

from app.blueprints.address.services.address_services import AddressService


def test_create_address_success():
    data = {
        "street": "123 Main St",
        "city": "Denver",
        "state": "CO",
        "zipcode": "80202",
        "country": "USA",
        "created_by_user_id": "user-1",
        "updated_by_user_id": None,
    }

    with patch(
        "app.blueprints.address.services.address_services.AddressRepository.create"
    ) as mock_create, patch(
        "app.blueprints.address.services.address_services.db.session.commit"
    ) as mock_commit:
        created_address = AddressService.create_address(data)

    assert created_address.street == "123 Main St"
    assert created_address.city == "Denver"
    assert created_address.state == "CO"
    assert created_address.zipcode == "80202"
    assert created_address.country == "USA"
    mock_create.assert_called_once()
    mock_commit.assert_called_once()


def test_create_address_integrity_error():
    data = {
        "street": "123 Main St",
        "city": "Denver",
        "state": "CO",
        "zipcode": "80202",
        "country": "USA",
        "created_by_user_id": "user-1",
        "updated_by_user_id": None,
    }

    with patch(
        "app.blueprints.address.services.address_services.AddressRepository.create",
        side_effect=IntegrityError("stmt", "params", "orig"),
    ), patch(
        "app.blueprints.address.services.address_services.db.session.rollback"
    ) as mock_rollback:
        with pytest.raises(
            ValueError,
            match="Address creation failed due to a database constraint",
        ):
            AddressService.create_address(data)

    mock_rollback.assert_called_once()


def test_create_address_generic_exception():
    data = {
        "street": "123 Main St",
        "city": "Denver",
        "state": "CO",
        "zipcode": "80202",
        "country": "USA",
        "created_by_user_id": "user-1",
        "updated_by_user_id": None,
    }

    with patch(
        "app.blueprints.address.services.address_services.AddressRepository.create",
        side_effect=Exception("DB error"),
    ), patch(
        "app.blueprints.address.services.address_services.db.session.rollback"
    ) as mock_rollback:
        with pytest.raises(Exception, match="DB error"):
            AddressService.create_address(data)

    mock_rollback.assert_called_once()
