from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class TokenSerializer(serializers.Serializer):
    token = serializers.SerializerMethodField()

    def create(self, validated_data):
        pass

    @staticmethod
    def get_token(user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def update(self, instance, validated_data):
        pass
