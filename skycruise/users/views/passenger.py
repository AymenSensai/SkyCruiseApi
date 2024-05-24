from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from skycruise.general.error import CustomExceptionHandlerMixin
from skycruise.users.models.user import Passenger
from skycruise.users.serializers.passenger import PassengerSerializer


class PassengerListCreateView(generics.ListCreateAPIView):
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Passenger.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PassengerUpdateView(CustomExceptionHandlerMixin, generics.RetrieveUpdateAPIView):
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated]
    queryset = Passenger.objects.all()

    def get_queryset(self):
        return Passenger.objects.filter(user=self.request.user)
