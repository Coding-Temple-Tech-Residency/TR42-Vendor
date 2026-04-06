import unittest
from unittest.mock import patch, MagicMock

from app.blueprints.vendor_user.services.vendor_user_services import VendorUserService
from app.blueprints.vendor_user.model import VendorUser, VendorUserRole


class TestVendorUserService(unittest.TestCase):

    @patch("app.blueprints.vendor_user.services.vendor_user_services.db.session.commit")
    @patch(
        "app.blueprints.vendor_user.services.vendor_user_services.VendorUserRepository"
    )
    def test_add_user_to_vendor_success(self, mock_repository, mock_commit):
        mock_repository.create.return_value = MagicMock(spec=VendorUser)

        data = {
            "user_id": "user123",
            "vendor_id": "vendor456",
            "vendor_user_role": "admin",
            "created_by_user_id": "creator789",
            "updated_by_user_id": "updater789",
        }

        result = VendorUserService.add_user_to_vendor(data)

        assert result is not None
        mock_repository.create.assert_called_once()
        mock_commit.assert_called_once()

    @patch("app.blueprints.vendor_user.services.vendor_user_services.db.session.commit")
    @patch(
        "app.blueprints.vendor_user.services.vendor_user_services.VendorUserRepository"
    )
    def test_add_user_repository_called_with_vendor_user(
        self, mock_repository, mock_commit
    ):
        mock_repository.create.return_value = MagicMock(spec=VendorUser)

        data = {
            "user_id": "user123",
            "vendor_id": "vendor456",
            "vendor_user_role": "admin",
            "created_by_user_id": "creator",
            "updated_by_user_id": "updater",
        }

        VendorUserService.add_user_to_vendor(data)

        call_args = mock_repository.create.call_args[0][0]
        assert isinstance(call_args, VendorUser)
        assert call_args.user_id == "user123"
        assert call_args.vendor_id == "vendor456"
        assert call_args.vendor_user_role == VendorUserRole.ADMIN

    @patch(
        "app.blueprints.vendor_user.services.vendor_user_services.VendorUserRepository"
    )
    def test_get_all_users_success(self, mock_repository):
        mock_users = [MagicMock(spec=VendorUser), MagicMock(spec=VendorUser)]
        mock_repository.get_all.return_value = mock_users

        result = VendorUserService.get_all_users()

        assert result == mock_users
        assert len(result) == 2
        mock_repository.get_all.assert_called_once()

    @patch(
        "app.blueprints.vendor_user.services.vendor_user_services.VendorUserRepository"
    )
    def test_get_all_users_empty(self, mock_repository):
        mock_repository.get_all.return_value = []

        result = VendorUserService.get_all_users()

        assert result == []
        mock_repository.get_all.assert_called_once()
