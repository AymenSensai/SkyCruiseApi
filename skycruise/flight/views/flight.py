from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from skycruise.flight.filters.flight import FlightFilter
from skycruise.flight.models.flight import Flight
from skycruise.flight.serializers.flight import FlightSerializer
from skycruise.general.error import get_error_request


class FlightView(APIView):

    def get(self, request, pk=None):
        if pk is None:
            airports = Flight.objects.all()
            serializer = FlightSerializer(airports, many=True)
            return Response(serializer.data)
        else:
            try:
                airport = Flight.objects.get(pk=pk)
                serializer = FlightSerializer(airport)
                return Response(serializer.data)
            except Flight.DoesNotExist:
                return get_error_request(message='Flight not found', status=status.HTTP_404_NOT_FOUND)


class FlightSearchView(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FlightFilter
