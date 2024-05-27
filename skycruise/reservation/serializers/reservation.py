from rest_framework import serializers

from skycruise.flight.models.flight import Flight, Seat
from skycruise.flight.serializers.flight import FlightSerializer, SeatSerializer
from skycruise.reservation.models.models import Reservation, ReservationSeat
from skycruise.users.models.user import Passenger
from skycruise.users.serializers.passenger import PassengerSerializer


class ReservationSeatSerializer(serializers.ModelSerializer):
    passenger = serializers.PrimaryKeyRelatedField(queryset=Passenger.objects.all())
    seat_number = serializers.CharField(write_only=True)
    seat_class = serializers.CharField(write_only=True)

    class Meta:
        model = ReservationSeat
        fields = ['id', 'passenger', 'seat_number', 'seat_class']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['seat_number'] = instance.seat.seat_number
        representation['seat_class'] = instance.seat.seat_class
        return representation


class ReservationSerializer(serializers.ModelSerializer):
    flight = serializers.PrimaryKeyRelatedField(queryset=Flight.objects.all())
    reservation_seats = ReservationSeatSerializer(many=True)
    number = serializers.CharField(read_only=True)

    class Meta:
        model = Reservation
        fields = ['id', 'flight', 'date', 'status', 'reservation_seats', 'number']
        read_only_fields = ['id', 'date', 'user', 'number']

    def create(self, validated_data):
        reservation_seats_data = validated_data.pop('reservation_seats', [])
        reservation = Reservation.objects.create(**validated_data)
        flight = validated_data['flight']

        for seat_data in reservation_seats_data:
            passenger = seat_data['passenger']
            seat_number = seat_data['seat_number']
            seat_class = seat_data['seat_class']

            seat, created = Seat.objects.get_or_create(
                seat_number=seat_number, flight=flight, defaults={
                    'is_available': False,
                    'seat_class': seat_class
                }
            )

            if not created and not seat.is_available:
                raise serializers.ValidationError(f'Seat {seat_number} is already taken.')

            if created:
                seat.is_available = False
                seat.save()

            ReservationSeat.objects.create(reservation=reservation, passenger=passenger, seat=seat)

        return reservation

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['flight'] = FlightSerializer(instance.flight).data
        return representation


class ReservationSeatReadSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(read_only=True)
    seat = SeatSerializer(read_only=True)

    class Meta:
        model = ReservationSeat
        fields = ['id', 'passenger', 'seat']


class ReservationReadSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only=True)
    reservation_seats = ReservationSeatReadSerializer(many=True, read_only=True)

    class Meta:
        model = Reservation
        fields = ['id', 'flight', 'date', 'status', 'reservation_seats', 'number']
        read_only_fields = ['id', 'date', 'user', 'number']
