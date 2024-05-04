from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

import authentication.urls
import users.urls

API_PREFIX = 'api/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(API_PREFIX, include(authentication.urls)),
    path(API_PREFIX, include(users.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
