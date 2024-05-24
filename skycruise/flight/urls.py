from django.urls import path

from skycruise.flight.views.flight import FlightSearchView, FlightView

urlpatterns = [
    path('flights', FlightView.as_view()),
    path('flight/<int:pk>', FlightView.as_view()),
    path('flight/search', FlightSearchView.as_view()),
]
