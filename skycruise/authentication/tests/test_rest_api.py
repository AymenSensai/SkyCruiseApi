import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.core import mail

User = get_user_model()


@pytest.mark.django_db
def test_login(api_client, bucky):
    url = '/api/auth/login'
    data = {'email': bucky.email, 'password': 'pass1234'}
    response = api_client.post(url, data, format='json')
    assert response.status_code == 200

    expected_authentication_keys = ['access_token', 'refresh_token']
    assert all(key in response.data for key in expected_authentication_keys)


@pytest.mark.django_db
def test_register(api_client):
    url = '/api/auth/register'
    data = {'email': 'newuser@example.com', 'username': 'newuser', 'password': 'newpassword123'}

    response = api_client.post(url, data, format='json')

    assert response.status_code == 200

    user = User.objects.get(email=data['email'])

    assert user.username == data['username']
    assert user.email == data['email']
    assert user.check_password(data['password'])

    expected_authentication_keys = ['access_token', 'refresh_token']
    assert all(key in response.data for key in expected_authentication_keys)


@pytest.mark.django_db
def test_send_email(api_client, bucky):
    user = bucky

    url = '/api/auth/sendEmail'
    data = {'email': user.email}

    response = api_client.post(url, data, format='json')

    assert response.status_code == 200

    assert len(mail.outbox) == 1
    email = mail.outbox[0]
    assert email.to == [user.email]
    assert email.subject == 'Password Reset Code'

    assert 'code' in response.data
    code = response.data['code']
    assert isinstance(code, int)
    assert 1000 <= code <= 9999


@pytest.mark.django_db
def test_password_reset(api_client, bucky):
    user = bucky

    url = '/api/auth/passwordReset'
    new_password = 'new_secure_password123'
    data = {'email': user.email, 'password': new_password}

    response = api_client.post(url, data, format='json')

    assert response.status_code == 200

    user.refresh_from_db()

    assert check_password(new_password, user.password)

    expected_authentication_keys = ['access_token', 'refresh_token']
    assert all(key in response.data for key in expected_authentication_keys)
