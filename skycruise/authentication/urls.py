from django.urls import path

from skycruise.authentication.views.login import LoginView
from skycruise.authentication.views.password_reset import PasswordResetView
from skycruise.authentication.views.register import RegisterView
from skycruise.authentication.views.send_email import SendEmailView

urlpatterns = [
    path('auth/login', LoginView.as_view(), name='login'),
    path('auth/register', RegisterView.as_view(), name='register'),
    path('auth/sendEmail', SendEmailView.as_view(), name='sendEmail'),
    path('auth/passwordReset', PasswordResetView.as_view(), name='passwordReset'),
]
