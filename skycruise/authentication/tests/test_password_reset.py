import pytest
from django.contrib.auth.hashers import check_password
from rest_framework import status

url = '/api/auth/passwordReset'


@pytest.mark.django_db
def test_password_reset_success(api_client, user):
    new_password = 'new_secure_password123'
    data = {'email': user.email, 'password': new_password}

    response = api_client.post(url, data, format='json')

    assert response.status_code == 200

    user.refresh_from_db()
    assert check_password(new_password, user.password)

    expected_authentication_keys = 'token'
    assert expected_authentication_keys in response.data


@pytest.mark.django_db
def test_password_reset_failure_missing_fields(api_client):
    # Missing email
    data = {'password': 'new_secure_password123'}
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'message' in response.data
    assert response.data['code'] == status.HTTP_400_BAD_REQUEST

    # Missing password
    data = {'email': 'user@example.com'}
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'message' in response.data
    assert response.data['code'] == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_password_reset_failure_invalid_email(api_client):
    data = {'email': 'invalid-email', 'password': 'new_secure_password123'}

    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'message' in response.data
    assert response.data['code'] == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_password_reset_failure_email_not_found(api_client):
    data = {'email': 'nonexistent@example.com', 'password': 'new_secure_password123'}

    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'message' in response.data
