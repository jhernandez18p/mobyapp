import os
from decouple import config
from django.contrib.messages import constants as message_constants
from django.contrib.messages import constants as messages

SITE_ID = 1

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['localhost','moby.dev2tech.xyz','*']

DJANGO_APPS = (
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
    # 'django.contrib.gis',
)

LOCAL_APPS = (
    'src.base',
    'src.blog',
    'src.gallery',
    'src.intra',
    'src.services',
    'src.support',
    'src.user',
    'src.ventas',
)

THIRD_PARTY_APPS = (
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader',
    'import_export',
    'widget_tweaks',
    'social_django',
    'sorl.thumbnail',
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
    'django.middleware.locale.LocaleMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
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
    'frontend': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.join(BASE_DIR, 'dbs'), 'db.sqlite3'),
    },
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_USER_PASSWORD'),
        'PORT': config('DB_PORT'),
        'HOST': config('DB_HOST'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
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
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'app.settings.EmailBackend.EmailBackend',
]

LANGUAGE_CODE = 'es-PA'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.join(BASE_DIR,os.pardir), 'media')

STATIC_URL = '/static/'


if config('STATIC_ROOT', cast=bool) == True:
    STATIC_ROOT = os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir), 'staticfiles'))
else:
    STATICFILES_DIRS = (os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir), 'staticfiles')),)

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

EMAIL_HOST = config('EMAIL_HOST')

EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

EMAIL_HOST_USER = config('EMAIL_HOST_USER')

EMAIL_PORT = config('EMAIL_PORT')

EMAIL_USE_SSL = config('EMAIL_USE_SSL',cast=bool)

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

EMAIL_TO_USER = EMAIL_HOST_USER

LOGIN_URL = '/auth/login/'

LOGIN_REDIRECT_URL = '/intra/'

SITE_URL = 'http://www.moby-group.com'

LOGOUT_REDIRECT_URL = SITE_URL

SESSION_COOKIE_AGE = 43200

SESSION_COOKIE_NAME = 'session'

PASSWORD_RESET_TIMEOUT_DAYS = 3

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
    messages.DEBUG: 'info',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

IMPORT_EXPORT_USE_TRANSACTIONS = True

APPEND_SLASH = True

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'
# CKEDITOR_CONFIGS = {
#     'default': {
#         'skin': 'Moono-Lisa',
#         # 'skin': 'office2013',
#         'toolbar_Basic': [
#             ['Source', '-', 'Bold', 'Italic']
#         ],
#         'toolbar_YourCustomToolbarConfig': [
#             {'name': 'document', 'items': ['Source', '-', 'Save', 'Print', '-', 'Templates']},
#             {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
#             {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
#             {'name': 'forms',
#              'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
#                        'HiddenField']},
#             '/',
#             {'name': 'basicstyles',
#              'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
#             {'name': 'paragraph',
#              'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
#                        'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
#                        'Language']},
#             {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
#             {'name': 'insert',
#              'items': ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
#             {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
#             {'name': 'colors', 'items': ['TextColor', 'BGColor']},
#             {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
#             {'name': 'about', 'items': ['About']},
#             '/',  # put this to force next toolbar on new line
#             {'name': 'yourcustomtools', 'items': [
#                 # put the name of your editor.ui.addButton here
#                 'Preview',
#                 'Maximize',
#                 'uploadfile',

#             ]},
#         ],
#         'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
#         # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
#         # 'height': 291,
#         # 'width': '100%',
#         # 'filebrowserWindowHeight': 725,
#         # 'filebrowserWindowWidth': 940,
#         # 'toolbarCanCollapse': True,
#         # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
#         'tabSpaces': 4,
#         'extraPlugins': ','.join([
#             'uploadimage', # the upload image feature
#             # your extra plugins here
#             'div',
#             'autolink',
#             'autoembed',
#             'embedsemantic',
#             'autogrow',
#             # 'devtools',
#             'widget',
#             'lineutils',
#             'clipboard',
#             'dialog',
#             'dialogui',
#             'elementspath'
#         ]),
#     }
# }

GOOGLE_RECAPTCHA_SECRET_KEY = config('GOOGLE_SECRET_KEY')