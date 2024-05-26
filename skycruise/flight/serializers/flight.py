from rest_framework import serializers

from skycruise.airline.serializers.airline import AirlineSerializer
from skycruise.flight.models.flight import Flight, FlightDetails, FlightStepover, Seat
from skycruise.location.serializers.airport import AirportSerializer


class FlightDetailsSerializer(serializers.ModelSerializer):
    airport = AirportSerializer(read_only=True)

    class Meta:
        model = FlightDetails
        fields = ['airport', 'terminal', 'gate', 'date']


class FlightStepoverSerializer(serializers.ModelSerializer):
    departure = FlightDetailsSerializer(read_only=True)
    arrival = FlightDetailsSerializer(read_only=True)

    class Meta:
        model = FlightStepover
        fields = ['departure', 'arrival']


class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat
        fields = ['seat_class', 'seat_number','seat_number', 'is_available']


class FlightSerializer(serializers.ModelSerializer):
    departure = FlightDetailsSerializer(read_only=True)
    arrival = FlightDetailsSerializer(read_only=True)
    airline = AirlineSerializer(read_only=True)
    stepovers = FlightStepoverSerializer(many=True, read_only=True)

    class Meta:
        model = Flight
        fields = [
            'id', 'flight_number', 'flight_status', 'airline', 'departure', 'arrival', 'price',
            'travel_insurance_price', 'tax_price', 'stepovers'
        ]
