import random

from django.db import models

from skycruise.flight.models.flight import Flight, Seat
from skycruise.users.models.user import Passenger, User


class Reservation(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reservations')
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='confirmed')
    number = models.CharField(max_length=12, unique=True, blank=True)

    def __str__(self):
        return f'Reservation {self.id} for Flight {self.flight.flight_number} by {self.user.username}'

    def save(self, *args, **kwargs):
        if not self.number:
            self.number = self.generate_number()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_number():
        return ''.join([str(random.randint(0, 9)) for _ in range(12)])


class ReservationSeat(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='reservation_seats')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='reservation_seats')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='reservation_seats')

    def __str__(self):
        return f'Seat {self.seat.seat_number} for Passenger {self.passenger.name} in Reservation {self.reservation.id}'
