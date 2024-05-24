from rest_framework import serializers

from skycruise.airline.models.airline import Airline


class AirlineSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name', read_only=True)

    class Meta:
        model = Airline
        fields = ['id', 'name', 'code', 'country_name', 'founded', 'logo']
        read_only_fields = ['country_name']
