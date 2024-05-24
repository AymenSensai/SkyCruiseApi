from django.contrib import admin

from skycruise.reservation.models.models import Reservation, ReservationSeat

admin.site.register([Reservation, ReservationSeat])
