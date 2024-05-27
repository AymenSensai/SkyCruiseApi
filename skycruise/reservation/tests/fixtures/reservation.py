import pytest
from model_bakery import baker

from skycruise.reservation.models.models import Reservation, ReservationSeat
from skycruise.users.models.user import Passenger


@pytest.fixture
def passenger(db):
    return baker.make(Passenger)


@pytest.fixture
def reservation(db, user, flight):
    return baker.make(Reservation, user=user, flight=flight)


@pytest.fixture
def reservation_seat(db, reservation, passenger, seat):
    return baker.make(ReservationSeat, reservation=reservation, passenger=passenger, seat=seat)
