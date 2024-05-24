from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from skycruise.airline.models.airline import Airline
from skycruise.airline.serializers.airline import AirlineSerializer
from skycruise.general.error import get_error_request


class AirlineView(APIView):

    def get(self, request, pk=None):
        if pk is None:
            airlines = Airline.objects.all()
            serializer = AirlineSerializer(airlines, many=True)
            return Response(serializer.data)
        else:
            try:
                airline = Airline.objects.get(pk=pk)
                serializer = AirlineSerializer(airline)
                return Response(serializer.data)
            except Airline.DoesNotExist:
                return get_error_request(message='Airline not found', status=status.HTTP_404_NOT_FOUND)
