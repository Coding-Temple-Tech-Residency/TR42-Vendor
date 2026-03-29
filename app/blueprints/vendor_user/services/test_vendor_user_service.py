import unittest
from unittest.mock import patch, MagicMock
from uuid import uuid4
from datetime import datetime
from app.blueprints.vendor_user.services.vendor_user_service import VendorUserService
from app.blueprints.vendor_user.model import VendorUser

class TestVendorUserService(unittest.TestCase):

    @patch('app.blueprints.vendor_user.services.vendor_user_service.VendorUserRepository')
    @patch('app.blueprints.vendor_user.services.vendor_user_service.uuid.uuid4')
    def test_create_user_success(self, mock_uuid, mock_repository):
        mock_uuid.return_value = uuid4()
        mock_repository.create.return_value = MagicMock()
        
        data = {
            "user_id": "user123",
            "vendor_id": "vendor456",
            "role": "admin",
            "created_by": "creator789",
            "updated_by": "updater789"
        }
        
        result = VendorUserService.create_user(data)
        
        assert result is not None
        mock_repository.create.assert_called_once()

    @patch('app.blueprints.vendor_user.services.vendor_user_service.VendorUserRepository')
    def test_create_user_with_missing_fields(self, mock_repository):
        mock_repository.create.return_value = MagicMock()
        
        data = {"user_id": "user123"}
        
        result = VendorUserService.create_user(data)
        
        assert result is not None
        mock_repository.create.assert_called_once()
    
    @patch('app.blueprints.vendor_user.services.vendor_user_service.VendorUserRepository')
    def test_create_user_repository_called_with_vendor_user(self, mock_repository):
        mock_repository.create.return_value = MagicMock()
        
        data = {
            "user_id": "user123",
            "vendor_id": "vendor456",
            "role": "manager",
            "created_by": "creator",
            "updated_by": "updater"
        }
        
        VendorUserService.create_user(data)
        
        call_args = mock_repository.create.call_args[0][0]
        assert isinstance(call_args, VendorUser)
        assert call_args.user_id == "user123"
        assert call_args.vendor_id == "vendor456"
        assert call_args.role == "manager"

        @patch('app.blueprints.vendor_user.services.vendor_user_service.VendorUserRepository')
        def test_get_all_users_success(self, mock_repository):
            mock_users = [MagicMock(), MagicMock()]
            mock_repository.get_all.return_value = mock_users
            
            result = VendorUserService.get_all_users()
            
            assert result == mock_users
            assert len(result) == 2
            mock_repository.get_all.assert_called_once()

        @patch('app.blueprints.vendor_user.services.vendor_user_service.VendorUserRepository')
        def test_get_all_users_empty(self, mock_repository):
            mock_repository.get_all.return_value = []
            
            result = VendorUserService.get_all_users()
            
            assert result == []
            mock_repository.get_all.assert_called_once()


if __name__ == '__main__':
    unittest.main()