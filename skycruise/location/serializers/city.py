from rest_framework import serializers

from skycruise.location.models.models import City


class CitySerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name', read_only=True)

    class Meta:
        model = City
        fields = ['id', 'name', 'latitude', 'longitude', 'country_name']
