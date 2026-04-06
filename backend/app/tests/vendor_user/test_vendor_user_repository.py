import pytest
from unittest.mock import patch, MagicMock
from app.blueprints.vendor_user.repositories.vendor_user_repositories import (
    VendorUserRepository,
)


@pytest.fixture
def mock_vendor_user_query():
    with patch(
        "app.blueprints.vendor_user.repositories.vendor_user_repositories.VendorUser"
    ) as MockVendorUser:
        yield MockVendorUser


def test_get_all_returns_all_vendor_users(mock_vendor_user_query):
    mock_users = [MagicMock(), MagicMock()]
    mock_vendor_user_query.query.all.return_value = mock_users

    result = VendorUserRepository.get_all()

    assert result == mock_users
    mock_vendor_user_query.query.all.assert_called_once()


def test_get_all_returns_empty_list_when_no_users(mock_vendor_user_query):
    mock_vendor_user_query.query.all.return_value = []

    result = VendorUserRepository.get_all()

    assert result == []
    mock_vendor_user_query.query.all.assert_called_once()


@patch("app.blueprints.vendor_user.repositories.vendor_user_repositories.db")
def test_create_adds_vendor_user(mock_db):
    mock_vendor_user = MagicMock()

    result = VendorUserRepository.create(mock_vendor_user)

    mock_db.session.add.assert_called_once_with(mock_vendor_user)
    assert result == mock_vendor_user


@patch("app.blueprints.vendor_user.repositories.vendor_user_repositories.db")
def test_create_raises_exception_on_db_error(mock_db):
    mock_vendor_user = MagicMock()
    mock_db.session.add.side_effect = Exception("DB Error")

    with pytest.raises(Exception) as exc_info:
        VendorUserRepository.create(mock_vendor_user)

    assert "DB Error" in str(exc_info.value)
    mock_db.session.add.assert_called_once_with(mock_vendor_user)
