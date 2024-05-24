from django.urls import path

from skycruise.location.views.airport import AirportView
from skycruise.location.views.city import CityView
from skycruise.location.views.country import CountryView

urlpatterns = [
    path('countries', CountryView.as_view()),
    path('country/<int:pk>', CountryView.as_view()),
    path('cities', CityView.as_view()),
    path('city/<int:pk>', CityView.as_view()),
    path('airports', AirportView.as_view()),
    path('airport/<int:pk>', AirportView.as_view()),
]
