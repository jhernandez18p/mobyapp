import os

from decouple import config

# Site ID
SITE_ID = 1
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['159.89.242.198','moby.dev2tech.xyz','127.0.0.1']
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
)
LOCAL_APPS = (
    'src.base',
    'src.intra',
)
THIRD_PARTY_APPS = (
    'rest_framework',
)
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
# Middleware SetUp
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]
# Site conf
ROOT_URLCONF = 'app.urls.base'
WSGI_APPLICATION = 'app.wsgi.application'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.abspath(os.path.join(os.path.join(BASE_DIR, os.pardir), 'templates')),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'app.settings.custom_context_processors.menu',
            ],
        },
    },
]
# Database
if config('DEBUG'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(os.path.join(BASE_DIR,'databases'), 'local.sqlite3'),
        },
        'frontend':{
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(os.path.join(BASE_DIR,'databases'), 'frontend.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('DB_ENGINE'),
            'USER': config('DB_NAME'),
            'PASSWORD': config('DB_USER'),
            'HOST': config('DB_USER_PASSWORD'),
            'PORT': config('DB_PORT'),
        }
    }
# Security Conf
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'app.settings.EmailBackend.EmailBackend',
)
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = 'es-pa'
# TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# Django Rest Framework Setup
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}
# Email Conf.
# EMAIL_HOST = config("EMAIL_HOST",)
# EMAIL_PORT = config("EMAIL_PORT", cast=int)
# EMAIL_HOST_USER = config("EMAIL_HOST_USER",)
# EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD",)
# EMAIL_USE_SSL = config("EMAIL_USE_SSL", cast=bool)
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'https://www.moby-group.com/'
SESSION_COOKIE_AGE = 43200
SESSION_COOKIE_NAME = 'session'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# Media Configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.abspath(os.path.join(os.path.join(BASE_DIR, os.pardir), 'media'))
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'
if config('STATIC'):
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
else:
    STATICFILES_DIRS = (
        os.path.abspath(os.path.join(os.path.join(BASE_DIR, os.pardir), 'staticfiles')),
    )
# STATIC_ROOT = os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir),'staticfiles'))