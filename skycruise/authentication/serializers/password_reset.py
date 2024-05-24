from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(validators=[validate_password], write_only=True)

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise Exception('Email not found.')
        return value

    def save(self):
        email = self.validated_data['email']
        password = self.validated_data['password']
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
        return user
