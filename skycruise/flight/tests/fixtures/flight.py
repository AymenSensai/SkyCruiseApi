import pytest
from model_bakery import baker

from skycruise.flight.models.flight import Seat

@pytest.fixture
def sample_flight_1(sample_airline):
    departure_airport_1 = baker.make('location.Airport', code='DEP1')
    arrival_airport_1 = baker.make('location.Airport', code='ARR1')
    departure_details_1 = baker.make('flight.FlightDetails', airport=departure_airport_1, date='2024-05-27T08:00:00')
    arrival_details_1 = baker.make('flight.FlightDetails', airport=arrival_airport_1, date='2024-05-27T10:00:00')

    flight_1 = baker.make(
        'flight.Flight',
        flight_number='FLIGHT1',
        flight_status='scheduled',
        airline=sample_airline,
        departure=departure_details_1,
        arrival=arrival_details_1,
        price=100.00,
        travel_insurance_price=10.00,
        tax_price=5.00
    )

    return flight_1

@pytest.fixture
def sample_flight_2(sample_airline):
    departure_airport_2 = baker.make('location.Airport', code='DEP2')
    arrival_airport_2 = baker.make('location.Airport', code='ARR2')
    departure_details_2 = baker.make('flight.FlightDetails', airport=departure_airport_2, date='2024-05-28T08:00:00')
    arrival_details_2 = baker.make('flight.FlightDetails', airport=arrival_airport_2, date='2024-05-28T10:00:00')

    flight_2 = baker.make(
        'flight.Flight',
        flight_number='FLIGHT2',
        flight_status='scheduled',
        airline=sample_airline,
        departure=departure_details_2,
        arrival=arrival_details_2,
        price=120.00,
        travel_insurance_price=15.00,
        tax_price=7.00
    )
    return flight_2


@pytest.fixture
def seat(db, flight):
    return baker.make(Seat, flight=flight)