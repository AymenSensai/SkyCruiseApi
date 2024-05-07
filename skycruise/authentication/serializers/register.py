from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(validators=[validate_password], write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.pop('password')

        user = User.objects.create_user(username=username, password=password, email=email)

        return user

    @staticmethod
    def validate_username(value):
        if not value.isalnum():
            raise serializers.ValidationError('Usernames can only contain alphanumeric characters.')

        return value
