from .common import *

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', 'localhost']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1damd8z*n#66h#2h47+p&6gjqv01e9^a1cs8on^-6$)9kwwu_4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000'
]

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

INSTALLED_APPS += [
    'debug_toolbar',
    # 'silk',
    # 'elastic_panel',
    # 'django_elasticsearch_dsl',
    # 'django_elasticsearch_dsl_drf',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'silk.middleware.SilkyMiddleware',
    # 'debug_toolbar_force.middleware.ForceDebugToolbarMiddleware',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# INSTALLED_APPS += [
#     'cacheops',
# ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

DEBUG_TOOLBAR_PANELS = [
    # Defaults
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    # Additional
    # 'elastic_panel.panel.ElasticDebugPanel',
]

# Elasticsearch configuration
# ELASTICSEARCH_DSL = {
#     'default': {
#         'hosts': 'localhost:9200',
#         'timeout': 30,
#     },
# }

# # Name of the Elasticsearch index
# ELASTICSEARCH_INDEX_NAMES = {
#     'search.documents.profiles': 'dev_profiles',
#     # 'search.documents.groups': 'dev_groups',
# }

# # Name of the Elasticsearch inde
# ELASTICSEARCH_INDEX_NAMES = {
#     'search.documents.tag': 'dev_tag',
#     # ... others the same
# }

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     },
# }

# CACHEOPS_REDIS = "redis://127.0.0.1:6379/1"

# CACHEOPS_DEGRADE_ON_FAILURE = True

# CACHEOPS_DEFAULTS = {
#     'timeout': 60 * 60
# }

# CACHEOPS = {
#     'auth.user': {'ops': 'get', 'timeout': 60 * 15},
#     'auth.*': {'ops': ('fetch', 'get')},
#     'auth.permission': {'ops': 'all'},
#     'profiles.*': {'ops': 'all', 'timeout': 60 * 60},
#     'uploads.*': {'ops': 'all', 'timeout': 60 * 60},
#     'groups.*': {'ops': 'all', 'timeout': 60 * 60},
#     'search.*': {'ops': 'all', 'timeout': 60 * 60},
# }