import django_filters

from skycruise.flight.models.flight import Flight


class FlightFilter(django_filters.FilterSet):
    departure_airport = django_filters.CharFilter(field_name='departure__airport__code', lookup_expr='iexact')
    arrival_airport = django_filters.CharFilter(field_name='arrival__airport__code', lookup_expr='iexact')
    departure_date = django_filters.DateFilter(field_name='departure__date', lookup_expr='gte')
    arrival_date = django_filters.DateFilter(field_name='arrival__date', lookup_expr='lte')

    class Meta:
        model = Flight
        fields = ['departure_airport', 'arrival_airport', 'departure_date', 'arrival_date']
