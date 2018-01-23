import os
from decouple import config
from django.contrib.messages import constants as message_constants
from django.contrib.messages import constants as messages

# Site ID
SITE_ID = 1

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','moby.dev2tech.xyz','*']

# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django.contrib.redirects',
)

LOCAL_APPS = (
    'src.base',
    'src.blog',
    'src.intra',
    'src.user',
    'src.ventas',
)

THIRD_PARTY_APPS = (
    'rest_framework',
    'ckeditor',
    'widget_tweaks',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
]

ROOT_URLCONF = 'app.urls.base'

WSGI_APPLICATION = 'app.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':  [
            os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir), 'templates')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'app.settings.custom_context_processors.site',
                'app.settings.custom_context_processors.menu',
                'app.settings.custom_context_processors.sessions',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.join(BASE_DIR, 'dbs'), 'db.sqlite3'),
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'app.settings.EmailBackend.EmailBackend',
]

LANGUAGE_CODE = 'es-PA'

# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir), 'media'))

STATIC_URL = '/static/'


if config('STATIC_ROOT'):
    STATIC_ROOT = os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir), 'staticfiles'))
else:
    STATICFILES_DIRS = (
        os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir), 'staticfiles')),
    )


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

EMAIL_HOST = config('EMAIL_HOST')

EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

EMAIL_HOST_USER = config('EMAIL_HOST_USER')

EMAIL_PORT = config('EMAIL_PORT')

EMAIL_USE_SSL = config('EMAIL_USE_SSL')

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

LOGIN_URL = '/auth/login/'

LOGIN_REDIRECT_URL = '/intra/'

SITE_URL = 'http://www.dev2tech.xyz'

LOGOUT_REDIRECT_URL = SITE_URL

SESSION_COOKIE_AGE = 43200

SESSION_COOKIE_NAME = 'session'

# Django Rest Framework Setup
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}

MESSAGE_LEVEL = message_constants.INFO

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}