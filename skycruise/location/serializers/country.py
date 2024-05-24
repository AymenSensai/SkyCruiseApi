from rest_framework import serializers

from skycruise.location.models.models import Country


class CountrySerializer(serializers.ModelSerializer):
    capital_name = serializers.CharField(source='capital.name', read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'code', 'population', 'continent', 'currency_name', 'currency_code', 'capital_name']
