from unittest.mock import patch
from marshmallow import ValidationError


class MockAddress:
    def __init__(self):
        self.address_id = "123"
        self.street = "123 Main St"
        self.city = "Denver"
        self.state = "CO"
        self.zipcode = "80202"
        self.country = "USA"
        self.created_by_user_id = "user-1"
        self.updated_by_user_id = None


def test_create_address_success(client):
    payload = {
        "street": "123 Main St",
        "city": "Denver",
        "state": "CO",
        "zipcode": "80202",
        "country": "USA",
        "created_by_user_id": "user-1",
    }

    mock_address = MockAddress()

    with patch(
        "app.blueprints.address.controller.address_routes.address_schema.load",
        return_value=payload,
    ), patch(
        "app.blueprints.address.controller.address_routes.AddressService.create_address",
        return_value=mock_address,
    ), patch(
        "app.blueprints.address.controller.address_routes.address_schema.dump",
        return_value={
            "address_id": "123",
            "street": "123 Main St",
            "city": "Denver",
            "state": "CO",
            "zipcode": "80202",
            "country": "USA",
            "created_by_user_id": "user-1",
            "updated_by_user_id": None,
        },
    ):
        response = client.post("/addresses/", json=payload)

    assert response.status_code == 201
    data = response.get_json()
    assert data["street"] == "123 Main St"
    assert data["city"] == "Denver"
    assert data["state"] == "CO"
    assert data["zipcode"] == "80202"


def test_create_address_no_data(client):
    response = client.post("/addresses/", json={})

    assert response.status_code == 400
    assert response.get_json() == {"error": "No input data provided"}


def test_create_address_validation_error(client):
    payload = {
        "street": "",
        "city": "Denver",
        "state": "CO",
        "zipcode": "80202",
        "created_by_user_id": "user-1",
    }

    with patch(
        "app.blueprints.address.controller.address_routes.address_schema.load",
        side_effect=ValidationError({"street": ["Missing data for required field."]}),
    ):
        response = client.post("/addresses/", json=payload)

    assert response.status_code == 400
    assert response.get_json() == {
        "errors": {"street": ["Missing data for required field."]}
    }


def test_create_address_service_value_error(client):
    payload = {
        "street": "123 Main St",
        "city": "Denver",
        "state": "CO",
        "zipcode": "80202",
        "created_by_user_id": "user-1",
    }

    with patch(
        "app.blueprints.address.controller.address_routes.address_schema.load",
        return_value=payload,
    ), patch(
        "app.blueprints.address.controller.address_routes.AddressService.create_address",
        side_effect=ValueError("Address creation failed due to a database constraint"),
    ):
        response = client.post("/addresses/", json=payload)

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Address creation failed due to a database constraint"
    }


def test_create_address_service_exception(client):
    payload = {
        "street": "123 Main St",
        "city": "Denver",
        "state": "CO",
        "zipcode": "80202",
        "created_by_user_id": "user-1",
    }

    with patch(
        "app.blueprints.address.controller.address_routes.address_schema.load",
        return_value=payload,
    ), patch(
        "app.blueprints.address.controller.address_routes.AddressService.create_address",
        side_effect=Exception("DB error"),
    ):
        response = client.post("/addresses/", json=payload)

    assert response.status_code == 500
    assert response.get_json() == {"error": "Failed to create address"}
