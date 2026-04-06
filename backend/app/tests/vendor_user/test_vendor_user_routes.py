from unittest.mock import patch, MagicMock


def test_get_vendor_users_success(client):
    mock_users = [{"id": 1}, {"id": 2}]

    with patch(
        "app.blueprints.vendor_user.controller.vendor_user_routes.VendorUserService.get_all_users",
        return_value=mock_users,
    ), patch(
        "app.blueprints.vendor_user.controller.vendor_user_routes.vendor_users_schema.dump",
        return_value=mock_users,
    ):
        response = client.get("/vendor_users/")

    assert response.status_code == 200
    assert response.get_json() == mock_users


def test_get_vendor_users_exception(client):
    with patch(
        "app.blueprints.vendor_user.controller.vendor_user_routes.VendorUserService.get_all_users",
        side_effect=Exception("DB error"),
    ):
        response = client.get("/vendor_users/")

    assert response.status_code == 500
    assert response.get_json() == {"error": "An error occurred while fetching users"}


def test_create_vendor_user_success(client):
    mock_user = MagicMock()
    mock_user.id = 123

    user_data = {
        "user_id": "user123",
        "vendor_id": "vendor456",
        "vendor_user_role": "ADMIN",
        "created_by_user_id": "creator789",
        "updated_by_user_id": "updater789",
    }

    with patch(
        "app.blueprints.vendor_user.controller.vendor_user_routes.VendorUserService.add_user_to_vendor",
        return_value=mock_user,
    ), patch(
        "app.blueprints.vendor_user.controller.vendor_user_routes.vendor_user_schema.dump",
        return_value={"id": 123},
    ):
        response = client.post("/vendor_users/", json=user_data)

    assert response.status_code == 201
    assert response.get_json() == {"id": 123}


def test_create_vendor_user_exception(client):
    user_data = {
        "user_id": "user123",
        "vendor_id": "vendor456",
        "vendor_user_role": "ADMIN",
        "created_by_user_id": "creator789",
        "updated_by_user_id": "updater789",
    }

    with patch(
        "app.blueprints.vendor_user.controller.vendor_user_routes.VendorUserService.add_user_to_vendor",
        side_effect=Exception("Create error"),
    ):
        response = client.post("/vendor_users/", json=user_data)

    assert response.status_code == 500
    assert response.get_json() == {"error": "An error occurred while creating the user"}
