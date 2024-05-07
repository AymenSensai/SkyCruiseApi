from django.urls import path

from skycruise.authentication.views.login import LoginView
from skycruise.authentication.views.register import RegisterView

urlpatterns = [
    path('auth/login', LoginView.as_view()),
    path('auth/register', RegisterView.as_view()),
]
