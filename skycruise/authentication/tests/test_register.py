import pytest
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

url = '/api/auth/register'


@pytest.mark.django_db
def test_register(api_client):
    data = {'email': 'newuser@example.com', 'username': 'newuser', 'password': 'newpassword123'}

    response = api_client.post(url, data, format='json')

    assert response.status_code == 200

    user = User.objects.get(email=data['email'])

    assert user.username == data['username']
    assert user.email == data['email']
    assert user.check_password(data['password'])

    expected_authentication_keys = 'token'
    assert expected_authentication_keys in response.data


@pytest.mark.django_db
def test_register_failure_missing_fields(api_client):
    # Missing email
    data = {'username': 'newuser', 'password': 'newpassword123'}
    response = api_client.post(url, data, format='json')
    assert response.status_code == 400
    assert 'message' in response.data
    assert response.data['code'] == status.HTTP_400_BAD_REQUEST

    # Missing username
    data = {'email': 'newuser@example.com', 'password': 'newpassword123'}
    response = api_client.post(url, data, format='json')
    assert response.status_code == 400
    assert 'message' in response.data
    assert response.data['code'] == status.HTTP_400_BAD_REQUEST

    # Missing password
    data = {'email': 'newuser@example.com', 'username': 'newuser'}
    response = api_client.post(url, data, format='json')
    assert response.status_code == 400
    assert 'message' in response.data
    assert response.data['code'] == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_register_failure_invalid_email(api_client):
    data = {'email': 'invalid_email', 'username': 'newuser', 'password': 'newpassword123'}

    response = api_client.post(url, data, format='json')
    assert response.status_code == 400
    assert 'message' in response.data
    assert response.data['code'] == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_register_failure_already_registered_email(api_client, user):
    data = {'email': user.email, 'username': 'newuser', 'password': 'newpassword123'}
    response = api_client.post(url, data, format='json')
    assert response.status_code == 400
    assert 'message' in response.data
    assert response.data['code'] == status.HTTP_400_BAD_REQUEST
