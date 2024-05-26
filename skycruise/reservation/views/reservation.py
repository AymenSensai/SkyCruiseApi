from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from skycruise.general.error import CustomExceptionHandlerMixin
from skycruise.reservation.models.models import Reservation
from skycruise.reservation.serializers.reservation import ReservationReadSerializer, ReservationSerializer


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