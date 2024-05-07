from django.urls import path

from skycruise.users.views.profile_view import ProfileView

urlpatterns = [
    path('user/profile', ProfileView.as_view()),
]
