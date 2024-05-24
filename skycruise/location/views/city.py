from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from skycruise.general.error import get_error_request
from skycruise.location.models.models import City
from skycruise.location.serializers.city import CitySerializer


class CityView(APIView):

    def get(self, request, pk=None):
        if pk is None:
            cities = City.objects.all()
            serializer = CitySerializer(cities, many=True)
            return Response(serializer.data)
        else:
            try:
                city = City.objects.get(pk=pk)
                serializer = CitySerializer(city)
                return Response(serializer.data)
            except City.DoesNotExist:
                return get_error_request(message='City not found', status=status.HTTP_404_NOT_FOUND)
