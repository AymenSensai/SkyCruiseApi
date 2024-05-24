from rest_framework import serializers

from skycruise.users.models.user import Passenger


class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        fields = ['id', 'name', 'nationality', 'date_of_birth', 'gender', 'id_number']
        read_only_fields = ['user']
