# import pytest
# from rest_framework import status

# @pytest.mark.django_db
# def test_country_view_list(api_client, country):
#     url = '/api/countries'

#     response = api_client.get(url)
#     assert response.status_code == status.HTTP_200_OK
#     assert len(response.data) == 1
#     assert response.data[0]['name'] == country.name
#     assert response.data[0]['capital_name'] == country.capital.name

# @pytest.mark.django_db
# def test_get_single_country(api_client, country):
#     url = '/api/country/1'

#     response = api_client.get(url)
#     assert response.status_code == status.HTTP_200_OK
#     assert response.data['name'] == country.name
#     assert response.data['capital_name'] == country.capital.name

# @pytest.mark.django_db
# def test_get_nonexistent_country(api_client):
#     url = '/api/country/9999'

#     response = api_client.get(url)
#     assert response.status_code == status.HTTP_404_NOT_FOUND
