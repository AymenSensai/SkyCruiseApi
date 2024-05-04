from typing import List

from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers.user import UserManager

class User(AbstractUser):

    username = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.BooleanField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS: List[str] = []

    objects = UserManager()
