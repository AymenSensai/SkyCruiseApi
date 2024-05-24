import pytest
from django.contrib.auth import get_user_model
from django.core import mail
from rest_framework import status

User = get_user_model()

url = '/api/auth/sendEmail'


@pytest.mark.django_db
def test_send_email_success(api_client, user):
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
def test_send_email_failure_missing_email(api_client):
    data = {}

    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'message' in response.data
    assert response.data['code'] == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_send_email_failure_invalid_email(api_client):
    data = {'email': 'invalid-email'}

    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'message' in response.data
    assert response.data['code'] == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_send_email_failure_email_not_found(api_client):
    data = {'email': 'nonexistent@example.com'}

    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'message' in response.data
