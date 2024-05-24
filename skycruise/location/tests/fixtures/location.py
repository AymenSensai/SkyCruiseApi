# import pytest
# from model_bakery import baker

# from skycruise.location.models.models import City, Country

# @pytest.fixture
# def city(db):
#     return  baker.make(
#     City,
#     name='Test City',
#     country=baker.make(Country),
#     latitude=0.0,
#     longitude=0.0
# )

# @pytest.fixture
# def country(db, city):
#     Country.objects.all().delete()
#     return baker.make(
#         Country,
#         name='Test Country',
#         code='TC',
#         population=1000000,
#         continent='AS',
#         currency_name='Test Currency',
#         currency_code='TCU',
#         capital=city
#     )

# @pytest.fixture
# def cities(db, countries):
#     cities = baker.make(
#         'location.City',
#         _quantity=3,
#         name=baker.seq('City '),
#         country=baker.iterate(countries),
#         latitude=baker.seq(10.0, increment_by=1.0),
#         longitude=baker.seq(20.0, increment_by=1.0)
#     )

#     for i, country in enumerate(countries):
#         country.capital = cities[i]
#         country.save()

#     return cities

# @pytest.fixture
# def airports(db, cities):
#     return baker.make(
#         'location.Airport',
#         _quantity=3,
#         name=baker.seq('Airport '),
#         city=baker.iterate(cities),
#         code=baker.seq('AP'),
#         latitude=baker.seq(30.0, increment_by=1.0),
#         longitude=baker.seq(40.0, increment_by=1.0)
#     )
