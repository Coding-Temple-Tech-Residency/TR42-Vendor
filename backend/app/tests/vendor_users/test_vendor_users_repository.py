import pytest
from unittest.mock import patch, MagicMock
from app.blueprints.vendor_users.repositories.vendor_users_repository import VendorUserRepository

@pytest.fixture
def mock_vendor_user_query():
    with patch('app.blueprints.vendor_users.repositories.vendor_user_repository.VendorUser') as MockVendorUser:
        yield MockVendorUser

def test_get_all_returns_all_vendor_users(mock_vendor_user_query):
    # Arrange
    mock_users = [MagicMock(), MagicMock()]
    mock_vendor_user_query.query.all.return_value = mock_users

    # Act
    result = VendorUserRepository.get_all()

    # Assert
    assert result == mock_users
    mock_vendor_user_query.query.all.assert_called_once()

def test_get_all_returns_empty_list_when_no_users(mock_vendor_user_query):
    # Arrange
    mock_vendor_user_query.query.all.return_value = []

    # Act
    result = VendorUserRepository.get_all()

    # Assert
    assert result == []
    mock_vendor_user_query.query.all.assert_called_once()
    @patch('app.blueprints.vendor_user.repositories.vendor_users_repository.db')
    def test_create_adds_and_commits_vendor_user(mock_db):
        # Arrange
        mock_vendor_user = MagicMock()

        # Act
        result = VendorUserRepository.create(mock_vendor_user)

        # Assert
        mock_db.session.add.assert_called_once_with(mock_vendor_user)
        mock_db.session.commit.assert_called_once()
        assert result == mock_vendor_user

    @patch('app.blueprints.vendor_user.repositories.vendor_users_repository.db')
    def test_create_raises_exception_on_db_error(mock_db):
        # Arrange
        mock_vendor_user = MagicMock()
        mock_db.session.add.side_effect = Exception("DB Error")

        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            VendorUserRepository.create(mock_vendor_user)
        assert "DB Error" in str(exc_info.value)
        mock_db.session.add.assert_called_once_with(mock_vendor_user)
        mock_db.session.commit.assert_not_called()
