from datetime import timedelta
from typing import List

import cloudinary
import cloudinary.api
import cloudinary.uploader
import environ

env = environ.Env()
environ.Env.read_env()

DEBUG = False
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS: List[str] = ['*']
CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS: List[str] = ['https://skycruiseapi-production.up.railway.app']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    'whitenoise.runserver_nostatic',
    'cloudinary',

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
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

cloudinary.config(
    cloud_name=env('CLOUDINARY_CLOUD_NAME'),
    api_key=env('CLOUDINARY_API_KEY'),
    api_secret=env('CLOUDINARY_API_SECRET')
)
