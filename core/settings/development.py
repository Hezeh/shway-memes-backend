from .common import *

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', 'localhost']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1damd8z*n#66h#2h47+p&6gjqv01e9^a1cs8on^-6$)9kwwu_4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000'
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}