from datetime import timedelta
from typing import List

import dj_database_url
import environ

env = environ.Env()
environ.Env.read_env()

DEBUG = False
SECRET_KEY = 'django-insecure-#u$pk4&c&f11+v*h=_km$gz$&18*aw2)&f!87a-pc&(s20+vfs'

ALLOWED_HOSTS: List[str] = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    "whitenoise.runserver_nostatic",
    
    # Apps
    'skycruise.authentication.apps.AuthenticationConfig',
    'skycruise.general.apps.GeneralConfig',
    'skycruise.users.apps.UsersConfig',
    'skycruise.location.apps.LocationConfig',
    'skycruise.flight.apps.FlightConfig',
    'skycruise.airline.apps.AirlineConfig',
    'skycruise.reservation.apps.ReservationConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'skycruise.project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
}

WSGI_APPLICATION = 'skycruise.project.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'skycruise',
#         'USER': 'postgres',
#         'PASSWORD': 'admin',
#         'HOST': 'localhost',
#         'PORT': '5432',
#         'ATOMIC_REQUESTS': True,
#         'CONN_MAX_AGE': 600,
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": r'C:\Users\Aymen\Desktop\SkyCruiseApi\db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'users.User'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # type: ignore # noqa: F821

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # type: ignore # noqa: F821

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'bestaouiaymene@gmail.com'
EMAIL_HOST_PASSWORD = 'wxqt iyxj qsov aqfc'
PASSWORD_RESET_CODE_TIMEOUT_MINUTES = 15

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"