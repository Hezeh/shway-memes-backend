import os
import datetime
import environ
# import dj_email_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1damd8z*n#66h#2h47+p&6gjqv01e9^a1cs8on^-6$)9kwwu_4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'shwaymemes.com']

# Application definition

INSTALLED_APPS = [
    # External apps that need to be before django's
    'storages',
    'admin_interface',
    'colorfield',
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
    # 'rest_framework_swagger',
    # 'rest_auth',
    # 'rest_auth.registration',
    'corsheaders',
    'versatileimagefield',
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

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000'
]

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


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

'''
# Uncomment when running in Docker
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),  # set in docker-compose.yml
        'PORT': env('DATABASE_PORT')  # default postgres port
    }
}
'''

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

EMAIL_URL = os.environ.get("EMAIL_URL")
SENDGRID_USERNAME = os.environ.get("SENDGRID_USERNAME")
SENDGRID_PASSWORD = os.environ.get("SENDGRID_PASSWORD")
if not EMAIL_URL and SENDGRID_USERNAME and SENDGRID_PASSWORD:
    EMAIL_URL = "smtp://%s:%s@smtp.sendgrid.net:587/?tls=True" % (
        SENDGRID_USERNAME,
        SENDGRID_PASSWORD,
    )
# email_config = dj_email_url.parse(
#     EMAIL_URL or "console://demo@example.com:console@example/"
# )

# Email Config
EMAIL_FILE_PATH= os.environ.get("EMAIL_FILE_PATH")
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST= os.environ.get('EMAIL_HOST')
EMAIL_HOST_PASSWORD= os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT= os.environ.get('EMAIL_PORT')
#EMAIL_USE_TLS= os.environ.get('EMAIL_USE_TLS')
EMAIL_USE_SSL= os.environ.get('EMAIL_USE_SSL')

ENABLE_SSL = os.environ.get("ENABLE_SSL")  # Set to True in prod env

if ENABLE_SSL:
    SECURE_SSL_REDIRECT = not DEBUG

# The default max length for the display of the sender email address
DEFAULT_MAX_EMAIL_DISPLAY_NAME_LENGTH = 78

DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Google Cloud Storage configuration
GS_PROJECT_ID = os.environ.get("GS_PROJECT_ID")
GS_STORAGE_BUCKET_NAME = os.environ.get("GS_STORAGE_BUCKET_NAME")
GS_MEDIA_BUCKET_NAME = os.environ.get("GS_MEDIA_BUCKET_NAME")
GS_AUTO_CREATE_BUCKET = os.environ.get("GS_AUTO_CREATE_BUCKET")

# If GOOGLE_APPLICATION_CREDENTIALS is set there is no need to load OAuth token
if "GOOGLE_APPLICATION_CREDENTIALS" not in os.environ:
    GS_CREDENTIALS = os.environ.get("GS_CREDENTIALS")

if GS_STORAGE_BUCKET_NAME:
    STATICFILES_STORAGES = "storages.backends.gcloud.GoogleCloudStorage"

if GS_MEDIA_BUCKET_NAME:
    DEFUALT_FILE_STORAGE = "companies_data.core.storages.GCSMediaStorage"
    THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE

VERSATILEIMAGEFIELD_SETTINGS = {
    # The amount of time, in seconds, that references to created images
    # should be stored in the cache. Defaults to `2592000` (30 days)
    'cache_length': 2592000,
    # The name of the cache you'd like `django-versatileimagefield` to use.
    # Defaults to 'versatileimagefield_cache'. If no cache exists with the name
    # provided, the 'default' cache will be used instead.
    'cache_name': 'versatileimagefield_cache',
    # The save quality of modified JPEG images. More info here:
    # https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#jpeg
    # Defaults to 70
    'jpeg_resize_quality': 70,
    # The name of the top-level folder within storage classes to save all
    # sized images. Defaults to '__sized__'
    'sized_directory_name': '__sized__',
    # The name of the directory to save all filtered images within.
    # Defaults to '__filtered__':
    'filtered_directory_name': '__filtered__',
    # The name of the directory to save placeholder images within.
    # Defaults to '__placeholder__':
    'placeholder_directory_name': '__placeholder__',
    # Whether or not to create new images on-the-fly. Set this to `False` for
    # speedy performance but don't forget to 'pre-warm' to ensure they're
    # created and available at the appropriate URL.
    'create_images_on_demand': True,
    # A dot-notated python path string to a function that processes sized
    # image keys. Typically used to md5-ify the 'image key' portion of the
    # filename, giving each a uniform length.
    # `django-versatileimagefield` ships with two post processors:
    # 1. 'versatileimagefield.processors.md5' Returns a full length (32 char)
    #    md5 hash of `image_key`.
    # 2. 'versatileimagefield.processors.md5_16' Returns the first 16 chars
    #    of the 32 character md5 hash of `image_key`.
    # By default, image_keys are unprocessed. To write your own processor,
    # just define a function (that can be imported from your project's
    # python path) that takes a single argument, `image_key` and returns
    # a string.
    'image_key_post_processor': None,
    # Whether to create progressive JPEGs. Read more about progressive JPEGs
    # here: https://optimus.io/support/progressive-jpeg/
    'progressive_jpeg': False
}

VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'meme_shot': [
        ('full_size', 'url'),
        ('thumbnail', 'thumbnail__400x400'),
        ('medium_square_crop', 'crop__500x400'),
        ('small_square_crop', 'crop__50x50')
    ]
}

# CACHES = {
#     # read os.environ['CACHE_URL'] and raises ImproperlyConfigured exception if not found
#     'default': env.cache(),
#     # read os.environ['REDIS_URL']
#     'redis': env.cache('REDIS_URL')
# }

#CACHE_URL = 

INTERNAL_IPS = [
    '127.0.0.1',
]

GOOGLE_ANALYTICS_TRACKING_ID = os.environ.get("GOOGLE_ANALYTICS_TRACKING_ID")

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# CELERY SETTINGS
CELERY_BROKER_URL = (
    os.environ.get('CELERY_BROKER_URL', os.environ.get('CLOUDAMQP_URL'))
)
CELERY_TASK_ALWAYS_EAGER = not CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', None)


# from wsvincent
# production
# if ENVIRONMENT == 'production':
#     SECURE_BROWSER_XSS_FILTER = True
#     X_FRAME_OPTIONS = 'DENY'
#     SECURE_SSL_REDIRECT = True
#     SECURE_HSTS_SECONDS = 3600
#     SECURE_HSTS_INCLUDE_SUBD
#     SECURE_HSTS_PRELOAD = True
#     SECURE_CONTENT_TYPE_NOSNIFF = True
#     SESSION_COOKIE_SECURE = True
#     CSRF_COOKIE_SECURE = True
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
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

# ACCOUNT_AUTHENTICATION_METHOD = 'username'
# ACCOUNT_EMAIL_VERIFICATION = 'none'

AUTH_USER_MODEL = 'users.User'

# REST_AUTH_SERIALIZERS = {
#     "USER_DETAILS_SERIALIZER": "users.serializers.CustomUserDetailsSerializer",
# }
# REST_AUTH_REGISTER_SERIALIZERS = {
#     "REGISTER_SERIALIZER": "users.serializers.CustomRegisterSerializer",
# }

# REST_AUTH_SERIALIZERS = {
#     'USER_DETAILS_SERIALIZER': 'users.serializers.UserSerializer',
#     #'TOKEN_SERIALIZER': 'users.serializers.TokenSerializer'
# }

# REST_AUTH_REGISTER_SERIALIZERS = {
#     'REGISTER_SERIALIZER': 'users.serializers.CustomRegisterSerializer',
# }

# JWT settings
# JWT_AUTH = {
#     'JWT_ENCODE_HANDLER':
#     'rest_framework_jwt.utils.jwt_encode_handler',

#     'JWT_DECODE_HANDLER':
#     'rest_framework_jwt.utils.jwt_decode_handler',

#     'JWT_PAYLOAD_HANDLER':
#     'rest_framework_jwt.utils.jwt_payload_handler',

#     'JWT_PAYLOAD_GET_USER_ID_HANDLER':
#     'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

#     'JWT_RESPONSE_PAYLOAD_HANDLER':
#     'rest_framework_jwt.utils.jwt_response_payload_handler',

#     'JWT_SECRET_KEY': SECRET_KEY,
#     'JWT_GET_USER_SECRET_KEY': None,
#     'JWT_PUBLIC_KEY': None,
#     'JWT_ALGORITHM': 'HS256',
#     'JWT_VERIFY': True,
#     'JWT_VERIFY_EXPIRATION': True,
#     'JWT_LEEWAY': 0,
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
#     'JWT_AUDIENCE': None,
#     'JWT_ISSUER': None,

#     'JWT_ALLOW_REFRESH': False,
#     'JWT_REFRESH_EXPRIRATION_DELTA': datetime.timedelta(days=7),

#     'JWT_AUTH_HEADER_PREFIX': 'Bearer',
#     'JWT_AUTH_COOKIE': None,
# }

SWAGGER_SETTTINGS = {
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    'API_SORTER': 'alpha',
    'SHOW_REQUEST_HEADERS': True,
    'JSON_EDITOR': True
}

# REST_USE_JWT = True 
