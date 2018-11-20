import os
from decouple import config
from django.contrib.messages import constants as message_constants

SITE_ID = 1
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config('SECRET_KEY')
ROOT_URLCONF = 'app.urls.base'
WSGI_APPLICATION = 'app.wsgi.application'
DEBUG = config('DEBUG', cast=bool)

# LOGIN_URL = '/auth/login/'
# LOGIN_REDIRECT_URL = '/intra/'
SITE_URL = 'http://www.moby-group.com'
SESSION_COOKIE_AGE = 43200
SESSION_COOKIE_NAME = 'session'

MESSAGE_TAGS = {
    message_constants.DEBUG: 'info',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'danger',
}

if DEBUG:
    # Debug True
    CORS_ORIGIN_ALLOW_ALL = True
    ALLOWED_HOSTS = ['*']
    MESSAGE_LEVEL = message_constants.DEBUG
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    
else:
    # Debug False
    ALLOWED_HOSTS = ['www.moby-group.com','*']
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
    EMAIL_HOST = config('EMAIL_HOST')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_PORT = config('EMAIL_PORT')
    EMAIL_USE_SSL = config('EMAIL_USE_SSL',cast=bool)
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    EMAIL_TO_USER = EMAIL_HOST_USER
    LOGOUT_REDIRECT_URL = SITE_URL
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    PASSWORD_RESET_TIMEOUT_DAYS = 3
    MESSAGE_LEVEL = message_constants.INFO

CORS_ORIGIN_WHITELIST = (
    'localhost:15100',
    'localhost:9000',
    'localhost:3000',
)


DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django.contrib.redirects',
]

LOCAL_APPS = [
    'src.base',
    'src.blog',
    'src.faq',
    'src.gallery',
    'src.intra',
    'src.services',
    'src.support',
    'src.testimonials',
    'src.user',
    'src.ventas',
]

THIRD_PARTY_APPS = [
    'ckeditor_uploader',
    'ckeditor',
    'corsheaders', # JWT
    'django_filters',
    'import_export',
    'knox',
    'rest_framework.authtoken',
    'rest_framework',
    'social_django',
    'sorl.thumbnail',
    'storages',
    'widget_tweaks',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # JWT
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    # 'social_django.middleware.SocialAuthExceptionMiddleware',
]

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
                'app.settings.custom_context_processors.menu',
                'app.settings.custom_context_processors.sessions',
                'app.settings.custom_context_processors.site',
                'app.settings.custom_context_processors.user',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_USER_PASSWORD'),
        'PORT': config('DB_PORT'),
        'HOST': config('DB_HOST'),
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
USE_I18N = True
USE_L10N = True
USE_TZ = True

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_LOCATION = 'static'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
DEFAULT_FILE_STORAGE = 'app.settings.storage_backends.MediaStorage'  # <-- here is where we reference it


# STATIC_URL = '/static/'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.join(BASE_DIR,os.pardir), 'media')

if config('STATIC_ROOT', cast=bool) == True:
    STATIC_ROOT = os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir), 'staticfiles'))
else:
    STATICFILES_DIRS = (os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir), 'staticfiles')),)
    # STATICFILES_DIRS = [
    #     os.path.join(BASE_DIR, 'mysite/static'),
    # ]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'src.user.tokens.my_jwt_response_handler'
}


IMPORT_EXPORT_USE_TRANSACTIONS = True

APPEND_SLASH = True

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'

GOOGLE_RECAPTCHA_SECRET_KEY = config('GOOGLE_SECRET_KEY')