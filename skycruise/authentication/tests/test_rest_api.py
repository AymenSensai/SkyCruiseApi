import pytest


@pytest.mark.django_db
def test_login(api_client, bucky):
    url = '/api/auth/login'
    data = {'email': bucky.email, 'password': 'pass1234'}
    response = api_client.post(url, data, format='json')
    assert response.status_code == 200

    expected_keys = ['authentication']
    assert all(key in response.data for key in expected_keys)

    expected_authentication_keys = ['access_token', 'refresh_token']
    assert all(key in response.data['authentication'] for key in expected_authentication_keys)