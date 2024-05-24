from rest_framework import serializers

from skycruise.flight.models.flight import Flight, Seat
from skycruise.flight.serializers.flight import FlightSerializer
from skycruise.reservation.models.models import Reservation, ReservationSeat
from skycruise.users.models.user import Passenger


class ReservationSeatSerializer(serializers.ModelSerializer):
    passenger = serializers.PrimaryKeyRelatedField(queryset=Passenger.objects.all())
    seat = serializers.PrimaryKeyRelatedField(queryset=Seat.objects.all())

    class Meta:
        model = ReservationSeat
        fields = ['id', 'passenger', 'seat']


class ReservationSerializer(serializers.ModelSerializer):
    flight = serializers.PrimaryKeyRelatedField(queryset=Flight.objects.all())
    reservation_seats = ReservationSeatSerializer(many=True)

    class Meta:
        model = Reservation
        fields = ['id', 'flight', 'date', 'status', 'reservation_seats']
        read_only_fields = ['id', 'date', 'user']

    def create(self, validated_data):
        reservation_seats_data = validated_data.pop('reservation_seats', [])
        reservation = Reservation.objects.create(**validated_data)
        for seat_data in reservation_seats_data:
            ReservationSeat.objects.create(reservation=reservation, **seat_data)
        return reservation

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['flight'] = FlightSerializer(instance.flight).data
        return representation
