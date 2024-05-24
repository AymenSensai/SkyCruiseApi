from django.urls import path

from skycruise.airline.views.airline import AirlineView

urlpatterns = [
    path('airlines', AirlineView.as_view()),
    path('airline/<int:pk>', AirlineView.as_view()),
]
