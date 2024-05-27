import pytest
from rest_framework import status


@pytest.mark.django_db
def test_city_view_list(api_client, city):
    url = '/api/cities'

    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['name'] == city.name


@pytest.mark.django_db
def test_get_single_country(api_client, city):
    url = '/api/city/1'

    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == city.name


@pytest.mark.django_db
def test_get_nonexistent_country(api_client):
    url = '/api/city/9999'

    response = api_client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
