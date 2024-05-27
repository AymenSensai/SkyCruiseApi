import pytest
from rest_framework import status


@pytest.mark.django_db
def test_get_flights(api_client, sample_flight_1):
    url = '/api/flights'
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['flight_number'] == sample_flight_1.flight_number


@pytest.mark.django_db
def test_get_flight(api_client, sample_flight_1):
    url = f'/api/flight/{sample_flight_1.pk}'
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['flight_number'] == sample_flight_1.flight_number


@pytest.mark.django_db
def test_search_flights_by_departure_airport(api_client, sample_flight_1):
    url = '/api/flight/search'
    response = api_client.get(url, {'departure_airport': 'DEP1'})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['flight_number'] == sample_flight_1.flight_number


@pytest.mark.django_db
def test_search_flights_by_arrival_airport(api_client, sample_flight_2):
    url = '/api/flight/search'
    response = api_client.get(url, {'arrival_airport': 'ARR2'})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['flight_number'] == sample_flight_2.flight_number


@pytest.mark.django_db
def test_search_flights_by_departure_date(api_client, sample_flight_2):
    url = '/api/flight/search'
    response = api_client.get(url, {'departure_date': '2024-05-28'})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['flight_number'] == sample_flight_2.flight_number


@pytest.mark.django_db
def test_search_flights_by_arrival_date(api_client, sample_flight_1):
    url = '/api/flight/search'
    response = api_client.get(url, {'arrival_date': '2024-05-29'})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['flight_number'] == sample_flight_1.flight_number


@pytest.mark.django_db
def test_search_flights_combined_filters(api_client, sample_flight_2):
    url = '/api/flight/search'
    response = api_client.get(
        url, {
            'departure_airport': 'DEP2',
            'arrival_airport': 'ARR2',
            'departure_date': '2024-05-28',
            'arrival_date': '2024-05-29'
        }
    )

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['flight_number'] == sample_flight_2.flight_number


@pytest.mark.django_db
def test_search_flights_invalid_departure_airport(api_client):
    url = '/api/flight/search'
    response = api_client.get(url, {'departure_airport': 'INVALID'})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 0


@pytest.mark.django_db
def test_search_flights_invalid_arrival_airport(api_client):
    url = '/api/flight/search'
    response = api_client.get(url, {'arrival_airport': 'INVALID'})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 0


@pytest.mark.django_db
def test_search_flights_invalid_departure_date(api_client):
    url = '/api/flight/search'
    response = api_client.get(url, {'departure_date': 'INVALID_DATE'})

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_search_flights_invalid_arrival_date(api_client):
    url = '/api/flight/search'
    response = api_client.get(url, {'arrival_date': 'INVALID_DATE'})

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_get_non_existent_flight(api_client):
    url = '/api/flight/9999'
    response = api_client.get(url)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert 'message' in response.data
    assert response.data['code'] == status.HTTP_404_NOT_FOUND
