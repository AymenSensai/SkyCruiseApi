import random

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email
from rest_framework import serializers

from skycruise.project import settings

User = get_user_model()


class SendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    @staticmethod
    def validate_email(value):
        try:
            validate_email(value)
        except DjangoValidationError:
            raise Exception('Invalid email format.')
        if not User.objects.filter(email=value).exists():
            raise Exception('Email does not exist.')
        return value

    def save(self):
        email = self.validated_data['email']
        user = User.objects.get(email=email)
        code = random.randint(1000, 9999)

        subject = 'Password Reset Code'
        message = f"""
        Hello {user.username},

        Here's your temporary password reset code:

        {code}

        Please enter this code on the password reset page to reset your password.

        This code will expire in {settings.PASSWORD_RESET_CODE_TIMEOUT_MINUTES} minutes.

        Sincerely,

        The SkyCruise Team
        """

        send_mail(subject, message, 'from@example.com', [email], fail_silently=False)
        return code
