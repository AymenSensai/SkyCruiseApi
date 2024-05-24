from typing import List

from django.contrib.auth.models import AbstractUser
from django.db import models

from skycruise.flight.models.flight import Flight
from skycruise.users.managers.user import UserManager


class User(AbstractUser):

    username = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.BooleanField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS: List[str] = []

    objects = UserManager()

    saved_flights = models.ManyToManyField(Flight, related_name='saved_by_users', blank=True)


class Passenger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='passengers')
    name = models.CharField(max_length=40)
    nationality = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.BooleanField(null=True)
    id_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
