from unittest.mock import patch
from tests.integration_tests.conftest import login_as


@patch("services.user.user_service.UserService.get_user_by_email")
def test_login_success(mock_get_user_by_email, client, user):
    mock_get_user_by_email.return_value = user
    response = client.post(
        "/auth/login", json={"email": user.email, "password": "password123"}
    )
    assert response.status_code == 200
    assert b"Login sucessful" in response.data


@patch("services.user.user_service.UserService.get_user_by_email")
def test_login_invalid_email(mock_get_user_by_email, client):
    mock_get_user_by_email.return_value = None
    response = client.post(
        "/auth/login", json={"email": "nonexistent@example.com", "password": "whatever"}
    )
    assert response.status_code == 401


@patch("services.user.user_service.UserService.get_user_by_email")
def test_login_wrong_password(mock_get_user_by_email, client, user):
    mock_get_user_by_email.return_value = user
    response = client.post(
        "/auth/login", json={"email": user.email, "password": "wrongpassword"}
    )
    assert response.status_code == 401


def test_login_bad_request_missing_fields(client):
    response = client.post("/auth/login", json={"email": "onlyemail@example.com"})
    assert response.status_code == 400


@patch("flask_login.logout_user")
@patch("flask_login.utils._get_user")
def test_logout_success(mock__get_user, mock_logout_user, client, user):
    login_as(client, user)
    mock__get_user.return_value.is_authenticated = True

    response = client.post("/auth/logout")
    assert response.status_code == 200
    assert b"Logged out successfully" in response.data


@patch("flask_login.utils._get_user")
def test_logout_unauthorized(mock__get_user, client):
    mock__get_user.return_value.is_authenticated = False
    response = client.post("/auth/logout")
    assert response.status_code == 401
