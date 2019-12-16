import os
import datetime
import environ
# import dj_email_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition

INSTALLED_APPS = [
    # External apps that need to be before django's
    'storages',
    # 'admin_interface',
    # 'colorfield',
    # Django modules
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    # Local apps
    'users',
    'photos',
    'search',
    'profiles',

    # External apps
    'rest_framework',
    # 'rest_framework.authtoken',
    'rest_framework_swagger',
    # 'rest_auth',
    # 'rest_auth.registration',
    'corsheaders',
    # 'versatileimagefield',
]

SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# VERSATILEIMAGEFIELD_SETTINGS = {
#     # The amount of time, in seconds, that references to created images
#     # should be stored in the cache. Defaults to `2592000` (30 days)
#     'cache_length': 2592000,
#     # The name of the cache you'd like `django-versatileimagefield` to use.
#     # Defaults to 'versatileimagefield_cache'. If no cache exists with the name
#     # provided, the 'default' cache will be used instead.
#     'cache_name': 'versatileimagefield_cache',
#     # The save quality of modified JPEG images. More info here:
#     # https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#jpeg
#     # Defaults to 70
#     'jpeg_resize_quality': 70,
#     # The name of the top-level folder within storage classes to save all
#     # sized images. Defaults to '__sized__'
#     'sized_directory_name': '__sized__',
#     # The name of the directory to save all filtered images within.
#     # Defaults to '__filtered__':
#     'filtered_directory_name': '__filtered__',
#     # The name of the directory to save placeholder images within.
#     # Defaults to '__placeholder__':
#     'placeholder_directory_name': '__placeholder__',
#     # Whether or not to create new images on-the-fly. Set this to `False` for
#     # speedy performance but don't forget to 'pre-warm' to ensure they're
#     # created and available at the appropriate URL.
#     'create_images_on_demand': True,
#     # A dot-notated python path string to a function that processes sized
#     # image keys. Typically used to md5-ify the 'image key' portion of the
#     # filename, giving each a uniform length.
#     # `django-versatileimagefield` ships with two post processors:
#     # 1. 'versatileimagefield.processors.md5' Returns a full length (32 char)
#     #    md5 hash of `image_key`.
#     # 2. 'versatileimagefield.processors.md5_16' Returns the first 16 chars
#     #    of the 32 character md5 hash of `image_key`.
#     # By default, image_keys are unprocessed. To write your own processor,
#     # just define a function (that can be imported from your project's
#     # python path) that takes a single argument, `image_key` and returns
#     # a string.
#     'image_key_post_processor': None,
#     # Whether to create progressive JPEGs. Read more about progressive JPEGs
#     # here: https://optimus.io/support/progressive-jpeg/
#     'progressive_jpeg': False
# }

# VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
#     'meme_shot': [
#         ('full_size', 'url'),
#         ('thumbnail', 'thumbnail__400x400'),
#         ('medium_square_crop', 'crop__500x400'),
#         ('small_square_crop', 'crop__50x50')
#     ]
# }


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'users.backends.JWTAuthentication',
    ),
}

CSRF_COOKIE_NAME = "csrftoken"

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_EMAIL_FIELD = 'email'
ACCOUNT_LOGOUT_ON_GET = True

# ACCOUNT_EMAIL_VERIFICATION = 'none'

AUTH_USER_MODEL = 'users.User'

SWAGGER_SETTTINGS = {
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    'API_SORTER': 'alpha',
    'SHOW_REQUEST_HEADERS': True,
    'JSON_EDITOR': True
}

# REST_USE_JWT = True 
