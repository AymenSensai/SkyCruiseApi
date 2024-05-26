from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from skycruise.flight.models.flight import Flight
from skycruise.flight.serializers.flight import FlightSerializer
from skycruise.general.error import CustomExceptionHandlerMixin, get_error_request
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

class SavedFlightListView(CustomExceptionHandlerMixin, generics.ListAPIView):
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.saved_flights.all()


class SavedFlightAddView(CustomExceptionHandlerMixin, generics.CreateAPIView):
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        flight_id = self.kwargs.get('pk')
        try:
            flight = Flight.objects.get(id=flight_id)
            request.user.saved_flights.add(flight)
            return Response({'message': 'Flight added to saved flights.'}, status=status.HTTP_201_CREATED)
        except Flight.DoesNotExist:
            return get_error_request('Flight not found.', status=status.HTTP_404_NOT_FOUND)


class SavedFlightDeleteView(CustomExceptionHandlerMixin, generics.DestroyAPIView):
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated]
    queryset = Flight.objects.all()

    def get_queryset(self):
        user = self.request.user
        return user.saved_flights.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        user.saved_flights.remove(instance)
        return Response({'message': 'Flight removed from saved flights.'}, status=status.HTTP_204_NO_CONTENT)
    

class CheckSavedFlightAPIView(CustomExceptionHandlerMixin, APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, flight_id):
        flight = get_object_or_404(Flight, pk=flight_id)
        
        user = request.user

        is_saved = flight.saved_by_users.filter(pk=user.pk).exists()

        if not is_saved:
            return get_error_request('Flight is not saved by the user.', status.HTTP_400_BAD_REQUEST)

        return Response({'is_saved': is_saved}, status=status.HTTP_200_OK)
