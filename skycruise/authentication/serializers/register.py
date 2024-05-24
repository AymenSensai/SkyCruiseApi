from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.validators import validate_email
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(validators=[validate_password], write_only=True)
    email = serializers.CharField()

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
            raise Exception('Usernames can only contain alphanumeric characters.')
        return value

    @staticmethod
    def validate_email(value):
        try:
            validate_email(value)
        except DjangoValidationError:
            raise Exception('Invalid email format.')
        if User.objects.filter(email=value).exists():
            raise Exception('A user with this email already exists.')
        return value
