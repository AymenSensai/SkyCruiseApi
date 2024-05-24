from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from skycruise.users.models import User
from skycruise.users.models.user import Passenger

admin.site.register(User, UserAdmin)
admin.site.register(Passenger)
