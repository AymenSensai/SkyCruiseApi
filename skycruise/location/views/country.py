from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from skycruise.general.error import get_error_request
from skycruise.location.models.models import Country
from skycruise.location.serializers.country import CountrySerializer


class CountryView(APIView):

    def get(self, request, pk=None):
        if pk is None:
            countries = Country.objects.all()
            serializer = CountrySerializer(countries, many=True)
            return Response(serializer.data)
        else:
            try:
                country = Country.objects.get(pk=pk)
                serializer = CountrySerializer(country)
                return Response(serializer.data)
            except Country.DoesNotExist:
                return get_error_request(message='Country not found', status=status.HTTP_404_NOT_FOUND)
