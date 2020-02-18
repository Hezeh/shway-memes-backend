from .common import *
import environ

env = environ.Env(GS_BUCKET_NAME=(str, None))

env.read_env(os.environ.get("ENV_PATH", ".env"))

root = environ.Path(__file__) - 3
SITE_ROOT = root()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# handle raw host(s), or http(s):// host(s), or no host. 
if 'CURRENT_HOST' in os.environ:
    CURRENT_HOST = os.environ['CURRENT_HOST']
    HOSTS = []
    for h in CURRENT_HOST.split(','):
        if '://' in h:
            h = h.split('://')[1]
        HOSTS.append(h)
else:
    HOSTS = ["localhost"]

ALLOWED_HOSTS = ["127.0.0.1", 'api.shwaymemes.com'] + HOSTS
# SECURITY WARNING: update this when you have the production host
# ALLOWED_HOSTS = ['api.shwaymemes.com'] + HOSTS

DATABASES = {"default": env.db()}

# Set the cors whitelist for the frontend host
CORS_ORIGIN_WHITELIST = [
    'https://shwaymemes.com'
]

INTERNAL_IPS = [
    'api.shwaymemes.com'
] + HOSTS

STATIC_ROOT = "/static/"

GS_BUCKET_NAME = env("GS_BUCKET_NAME", None)

if GS_BUCKET_NAME:
    DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
    STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
    GS_DEFAULT_ACL = "publicRead"

    STATIC_HOST = "https://storage.googleapis.com/{GS_BUCKET_NAME}/"
    STATIC_URL = f"{STATIC_HOST}/{SITE_ROOT}/"
    MEDIA_ROOT = STATIC_HOST + "media/"
    MEDIA_URL = STATIC_HOST + "media/"

else:
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

    STATIC_HOST = "/"
    STATIC_URL = "/static/"

    MEDIA_ROOT = "media/"  # where files are stored on the local FS (in this case)
    MEDIA_URL = "/media/"  # what is prepended to the image URL (in this case)

# Elasticsearch configuration
# ELASTICSEARCH_DSL = {
#     'default': {
#         'hosts': 'localhost:9200',
#         'timeout': 30,
#     },
# }

# # Google Cloud Storage configuration
# GS_PROJECT_ID = os.environ.get("GS_PROJECT_ID")
# GS_STORAGE_BUCKET_NAME = os.environ.get("GS_STORAGE_BUCKET_NAME")
# GS_MEDIA_BUCKET_NAME = os.environ.get("GS_MEDIA_BUCKET_NAME")
# GS_AUTO_CREATE_BUCKET = os.environ.get("GS_AUTO_CREATE_BUCKET")

# # If GOOGLE_APPLICATION_CREDENTIALS is set there is no need to load OAuth token
# if "GOOGLE_APPLICATION_CREDENTIALS" not in os.environ:
#     GS_CREDENTIALS = os.environ.get("GS_CREDENTIALS")

# if GS_STORAGE_BUCKET_NAME:
#     STATICFILES_STORAGES = "storages.backends.gcloud.GoogleCloudStorage"

# if GS_MEDIA_BUCKET_NAME:
#     DEFUALT_FILE_STORAGE = "django-memes.core.storages.GCSMediaStorage"
#     THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
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

# EMAIL_URL = os.environ.get("EMAIL_URL")
# SENDGRID_USERNAME = os.environ.get("SENDGRID_USERNAME")
# SENDGRID_PASSWORD = os.environ.get("SENDGRID_PASSWORD")
# if not EMAIL_URL and SENDGRID_USERNAME and SENDGRID_PASSWORD:
#     EMAIL_URL = "smtp://%s:%s@smtp.sendgrid.net:587/?tls=True" % (
#         SENDGRID_USERNAME,
#         SENDGRID_PASSWORD,
#     )
# # email_config = dj_email_url.parse(
# #     EMAIL_URL or "console://demo@example.com:console@example/"
# # )

# # Email Config
# EMAIL_FILE_PATH= os.environ.get("EMAIL_FILE_PATH")
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST= os.environ.get('EMAIL_HOST')
# EMAIL_HOST_PASSWORD= os.environ.get('EMAIL_HOST_PASSWORD')
# EMAIL_PORT= os.environ.get('EMAIL_PORT')
# EMAIL_USE_TLS= os.environ.get('EMAIL_USE_TLS')
# EMAIL_USE_SSL= os.environ.get('EMAIL_USE_SSL')

# ENABLE_SSL = os.environ.get("ENABLE_SSL")  # Set to True in prod env

# if ENABLE_SSL:
#     SECURE_SSL_REDIRECT = not DEBUG

# # The default max length for the display of the sender email address
# DEFAULT_MAX_EMAIL_DISPLAY_NAME_LENGTH = 78

# DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)

# CACHES = {
#     # read os.environ['CACHE_URL'] and raises ImproperlyConfigured exception if not found
#     'default': env.cache(),
#     # read os.environ['REDIS_URL']
#     'redis': env.cache('REDIS_URL')
# }

# INTERNAL_IPS = [
#     '127.0.0.1',
# ]

# MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# # CELERY SETTINGS
# CELERY_BROKER_URL = (
#     os.environ.get('CELERY_BROKER_URL', os.environ.get('CLOUDAMQP_URL'))
# )
# CELERY_TASK_ALWAYS_EAGER = not CELERY_BROKER_URL
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', None)


# django for professionals caching. There are other middlewares to consider
# so something to lookout for.
# CACHE_MIDDLEWARE_ALIAS = 'default'
# CACHE_MIDDLEWARE_SECONDS = 604800
# CACHE_MIDDLEWARE_KEY_PREFIX = ''


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'root': {
#         'level': 'INFO',
#         'handlers': ['all_log'],
#     },
#     'formatters': {
#         'verbose': {
#             'format': '\n%(levelname)s %(asctime)s [%(pathname)s:%(lineno)s] '
#                       '%(message)s'
#         },
#         'simple': {
#             'format': '\n%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler'
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#         },
#         'all_log': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': PROJECT_DIR("../../logs/all.log"),
#             'maxBytes': 1048576,
#             'backupCount': 99,
#             'formatter': 'verbose',
#         },
#         'django_log': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': PROJECT_DIR("../../logs/django.log"),
#             'maxBytes': 1048576,
#             'backupCount': 99,
#             'formatter': 'verbose',
#         },
#         'django_request_log': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': PROJECT_DIR("../../logs/django_request.log"),
#             'maxBytes': 1048576,
#             'backupCount': 99,
#             'formatter': 'verbose',
#         },
#         'django_elasticsearch_dsl_drf_log': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': PROJECT_DIR("../../logs/debug_toolbar_force.log"),
#             'maxBytes': 1048576,
#             'backupCount': 99,
#             'formatter': 'verbose',
#         },
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['django_request_log'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#         'django': {
#             'handlers': ['django_log'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'books': {
#             'handlers': ['console', 'django_elasticsearch_dsl_drf_log'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'django_elasticsearch_dsl_drf': {
#             'handlers': ['console', 'django_elasticsearch_dsl_drf_log'],
#             'level': 'DEBUG',
#             'propagate': True,
#         }
#     },
# }