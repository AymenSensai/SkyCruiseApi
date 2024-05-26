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

    def __str__(self):
        return f'Reservation {self.id} for Flight {self.flight.flight_number} by {self.user.username}'


class ReservationSeat(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='reservation_seats')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='reservation_seats')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='reservation_seats')

    def __str__(self):
        return f'Seat {self.seat.seat_number} for Passenger {self.passenger.name} in Reservation {self.reservation.id}'
