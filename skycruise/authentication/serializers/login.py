from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, attrs):
        user = authenticate(email=attrs.get('email'), password=attrs.get('password'))

        if not user:
            raise Exception('Incorrect username or password.')

        if not user.is_active:
            raise Exception('User is deactivated.')

        return {'user': user}
