from django.db import models

from skycruise.airline.models.airline import Airline
from skycruise.location.models.models import Airport


class FlightDetails(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    terminal = models.CharField(max_length=10, null=True, blank=True)
    gate = models.CharField(max_length=10, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)


class FlightStepover(models.Model):
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE, related_name='stepovers')
    departure = models.OneToOneField(
        FlightDetails, on_delete=models.CASCADE, related_name='stepover_departure_flights', null=True, blank=True
    )
    arrival = models.OneToOneField(
        FlightDetails, on_delete=models.CASCADE, related_name='stepover_arrival_flights', null=True, blank=True
    )

    def __str__(self):
        return f'Stepover from {self.departure.airport} to {self.arrival.airport}'


class Seat(models.Model):
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE, related_name='seats')
    seat_class = models.CharField(max_length=20)
    seat_number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.seat_class} class: {self.seat_number} seats'


class Flight(models.Model):
    STATUS_CHOICES = [('scheduled', 'Scheduled'), ('delayed', 'Delayed'), ('cancelled', 'Cancelled'),
                      ('departed', 'Departed'), ('in_air', 'In Air'), ('landed', 'Landed'), ('arrived', 'Arrived'),
                      ('diverted', 'Diverted'), ('unknown', 'Unknown')]

    flight_number = models.CharField(max_length=20)
    flight_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='flights')
    departure = models.OneToOneField(
        FlightDetails, on_delete=models.CASCADE, related_name='departure_flights', null=True, blank=True
    )
    arrival = models.OneToOneField(
        FlightDetails, on_delete=models.CASCADE, related_name='arrival_flights', null=True, blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    travel_insurance_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Flight {self.flight_number}: {self.departure.airport} to {self.arrival.airport}'
