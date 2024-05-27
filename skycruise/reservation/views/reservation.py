from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from skycruise.flight.models.flight import Flight
from skycruise.reservation.models.models import Reservation, ReservationSeat
from skycruise.reservation.serializers.reservation import (
    ReservationReadSerializer, ReservationSerializer, ReservedSeatSerializer
)


class ReservationListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ReservationSerializer
        return ReservationReadSerializer


class ReservationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ReservationSerializer
        return ReservationReadSerializer


class ReservedSeatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, flight_id):
        flight = Flight.objects.get(id=flight_id)
        reserved_seats = ReservationSeat.objects.filter(seat__flight=flight)
        serializer = ReservedSeatSerializer(reserved_seats, many=True)
        return Response(serializer.data)
