from django.contrib import admin

from skycruise.flight.models.flight import Flight, FlightDetails, FlightStepover, Seat

admin.site.register([Flight, FlightDetails, FlightStepover, Seat])
