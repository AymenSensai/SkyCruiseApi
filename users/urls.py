from django.urls import path
from users.views.profile import UserViewSet


urlpatterns = [
    path('user/profile', UserViewSet.as_view()),
]