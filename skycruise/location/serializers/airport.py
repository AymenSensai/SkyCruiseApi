from rest_framework import serializers

from skycruise.location.models.models import Airport


class AirportSerializer(serializers.ModelSerializer):
    city_name = serializers.SerializerMethodField()
    country_name = serializers.SerializerMethodField()

    class Meta:
        model = Airport
        fields = ['id', 'name', 'code', 'latitude', 'longitude', 'city_name', 'country_name']

    def get_city_name(self, obj):
        return obj.city.name

    def get_country_name(self, obj):
        return obj.city.country.name
