import pytest


@pytest.mark.django_db
def test_get_all_airports(api_client, airports):
    url = '/api/airports'
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 3
    assert response.data[0]['name'] == airports[0].name
    assert response.data[1]['name'] == airports[1].name
    assert response.data[2]['name'] == airports[2].name


@pytest.mark.django_db
def test_get_single_airport_success(api_client, airports):
    url = '/api/airport/1'
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data['name'] == airports[0].name
    assert response.data['code'] == airports[0].code


@pytest.mark.django_db
def test_get_single_airport_not_found(api_client):
    url = '/api/airport/9999'
    response = api_client.get(url)

    assert response.status_code == 404
    assert response.data['message'] == 'Airport not found'
