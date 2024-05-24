from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from skycruise.general.error import get_error_request
from skycruise.location.models.models import Airport
from skycruise.location.serializers.airport import AirportSerializer


class AirportView(APIView):

    def get(self, request, pk=None):
        if pk is None:
            airports = Airport.objects.all()
            serializer = AirportSerializer(airports, many=True)
            return Response(serializer.data)
        else:
            try:
                airport = Airport.objects.get(pk=pk)
                serializer = AirportSerializer(airport)
                return Response(serializer.data)
            except Airport.DoesNotExist:
                return get_error_request(message='Airport not found', status=status.HTTP_404_NOT_FOUND)
