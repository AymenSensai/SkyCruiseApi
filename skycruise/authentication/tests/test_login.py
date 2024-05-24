import pytest
from rest_framework import status

url = '/api/auth/login'


@pytest.mark.django_db
def test_login_success(api_client, user):
    data = {'email': user.email, 'password': 'pass1234'}
    response = api_client.post(url, data, format='json')
    assert response.status_code == 200

    expected_authentication_keys = 'token'
    assert expected_authentication_keys in response.data


@pytest.mark.django_db
def test_login_failure_invalid_password(api_client, user):
    data = {'email': user.email, 'password': 'wrongpassword'}
    response = api_client.post(url, data, format='json')

    assert response.status_code == 400
    assert 'message' in response.data
    assert response.data['code'] == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_login_failure_invalid_email(api_client):
    data = {'email': 'nonexistent@example.com', 'password': 'pass1234'}
    response = api_client.post(url, data, format='json')

    assert response.status_code == 400
    assert 'message' in response.data
    assert response.data['code'] == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_login_failure_missing_fields(api_client, user):
    # Missing password
    data = {'email': user.email}
    response = api_client.post(url, data, format='json')
    assert response.status_code == 400
    assert 'message' in response.data
    assert response.data['code'] == status.HTTP_400_BAD_REQUEST

    # Missing email
    data = {'password': 'pass1234'}
    response = api_client.post(url, data, format='json')
    assert response.status_code == 400
    assert 'message' in response.data
    assert response.data['code'] == status.HTTP_400_BAD_REQUEST
