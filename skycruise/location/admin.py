from django.contrib import admin

from skycruise.location.models.models import Airport, City, Country

admin.site.register([Country, City, Airport])
