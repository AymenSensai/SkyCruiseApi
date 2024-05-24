# import pytest

# @pytest.mark.django_db
# def test_get_all_airports(api_client, create_airports):
#     url = '/api/airports'
#     response = api_client.get(url)

#     assert response.status_code == 200
#     assert len(response.data) == 3
#     assert response.data[0]['name'] == 'JFK International Airport'
#     assert response.data[1]['name'] == 'Los Angeles International Airport'
#     assert response.data[2]['name'] == 'San Francisco International Airport'

# @pytest.mark.django_db
# def test_get_single_airport_success(api_client, create_airports):
#     airport = create_airports[0]
#     url = '/api/airport/1'
#     response = api_client.get(url)

#     assert response.status_code == 200
#     assert response.data['name'] == 'JFK International Airport'
#     assert response.data['code'] == 'JFK'

# @pytest.mark.django_db
# def test_get_single_airport_not_found(api_client):
#     url = '/api/airport/9999'
#     response = api_client.get(url)

#     assert response.status_code == 404
#     assert response.data['message'] == 'Airport not found'
