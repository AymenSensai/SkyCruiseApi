from django.db import models


class Country(models.Model):
    CONTINENT_CHOICES = [
        ('AF', 'Africa'),
        ('AN', 'Antarctica'),
        ('AS', 'Asia'),
        ('EU', 'Europe'),
        ('NA', 'North America'),
        ('OC', 'Oceania'),
        ('SA', 'South America'),
    ]

    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=3, unique=True)
    population = models.PositiveIntegerField()
    continent = models.CharField(max_length=2, choices=CONTINENT_CHOICES)
    currency_name = models.CharField(max_length=50)
    currency_code = models.CharField(max_length=3)
    capital = models.OneToOneField(
        'City', on_delete=models.SET_NULL, null=True, blank=True, related_name='capital_of_country'
    )

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'{self.name}, {self.country.name}'


class Airport(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'{self.name} ({self.code})'
