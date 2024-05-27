import pytest
from model_bakery import baker

from skycruise.airline.models.airline import Airline


@pytest.fixture
def sample_airline(country):
    return baker.make(
        Airline, name='Sample Airline', code='SA', country=country, founded='2020-01-01', logo='path/to/logo.png'
    )
