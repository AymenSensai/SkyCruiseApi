from django.urls import path

from skycruise.reservation.views.reservation import (
    ReservationListCreateView, ReservationRetrieveUpdateDestroyView, ReservedSeatsView
)

urlpatterns = [
    path('reservations', ReservationListCreateView.as_view(), name='reservation-list-create'),
    path('reservations/<int:pk>', ReservationRetrieveUpdateDestroyView.as_view(), name='reservation-detail'),
    path('reservations/reserved-seats/<int:flight_id>', ReservedSeatsView.as_view(), name='reserved-seats'),
]
