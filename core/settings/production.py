from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', 'api.shwaymemes.com']

# Production Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT')  # default postgres port
    }
}

# Set the cors whitelist for the frontend host
CORS_ORIGIN_WHITELIST = [
    'https://shwaymemes.com'
]

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
EMAIL_USE_TLS= os.environ.get('EMAIL_USE_TLS')
EMAIL_USE_SSL= os.environ.get('EMAIL_USE_SSL')

ENABLE_SSL = os.environ.get("ENABLE_SSL")  # Set to True in prod env

if ENABLE_SSL:
    SECURE_SSL_REDIRECT = not DEBUG

# The default max length for the display of the sender email address
DEFAULT_MAX_EMAIL_DISPLAY_NAME_LENGTH = 78

DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)


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
    DEFUALT_FILE_STORAGE = "django-memes.core.storages.GCSMediaStorage"
    THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE

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
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# django for professionals caching. There are other middlewares to consider
# so something to lookout for.
# CACHE_MIDDLEWARE_ALIAS = 'default'
# CACHE_MIDDLEWARE_SECONDS = 604800
# CACHE_MIDDLEWARE_KEY_PREFIX = ''
