from django.urls import path

from skycruise.users.views.passenger import PassengerListCreateView, PassengerUpdateView
from skycruise.users.views.profile_view import ProfileView
from skycruise.users.views.saved_flight import (
    CheckSavedFlightAPIView, SavedFlightAddView, SavedFlightDeleteView, SavedFlightListView
)

urlpatterns = [
    path('user/profile', ProfileView.as_view()),
    path('user/passengers', PassengerListCreateView.as_view(), name='passenger-list-create'),
    path('user/passengers/<int:pk>', PassengerUpdateView.as_view(), name='passenger-update'),
    path('user/saved-flights', SavedFlightListView.as_view(), name='saved-flight-list'),
    path('user/saved-flights/add/<int:pk>', SavedFlightAddView.as_view(), name='saved-flight-add'),
    path('user/saved-flights/delete/<int:pk>', SavedFlightDeleteView.as_view(), name='saved-flight-delete'),
    path('user/check-saved-flight/<int:flight_id>', CheckSavedFlightAPIView.as_view(), name='check_saved_flight'),
]
