from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from skycruise.general.error import CustomExceptionHandlerMixin
from skycruise.reservation.models.models import Reservation
from skycruise.reservation.serializers.reservation import ReservationSerializer


class ReservationListCreateView(CustomExceptionHandlerMixin, generics.ListCreateAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReservationRetrieveUpdateDestroyView(CustomExceptionHandlerMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)
