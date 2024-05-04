from django.urls import path
from authentication.views.login import LoginView
from authentication.views.register import RegisterView

urlpatterns = [
    path('auth/login', LoginView.as_view()),
    path('auth/register', RegisterView.as_view()),
]
