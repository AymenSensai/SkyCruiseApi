from cloudinary.models import CloudinaryField
from django.db import models

from skycruise.location.models.models import Country


class Airline(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='airlines')
    founded = models.DateField(null=True, blank=True)
    logo = CloudinaryField('airline_logos')

    def __str__(self):
        return self.name
