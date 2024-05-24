from django.urls import path

from skycruise.reservation.views.reservation import ReservationListCreateView, ReservationRetrieveUpdateDestroyView

urlpatterns = [
    path('reservations', ReservationListCreateView.as_view(), name='reservation-list-create'),
    path('reservations/<int:pk>', ReservationRetrieveUpdateDestroyView.as_view(), name='reservation-detail'),
]
