import pytest
from rest_framework import status


@pytest.mark.django_db
def test_get_airlines(api_client, sample_airline):
    url = '/api/airlines'
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['name'] == sample_airline.name


@pytest.mark.django_db
def test_get_airline(api_client, sample_airline):
    url = f'/api/airline/{sample_airline.pk}'
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == sample_airline.name
