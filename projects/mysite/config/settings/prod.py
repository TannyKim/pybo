from .base import *

ALLOWED_HOSTS = ['54.180.54.179', 'tandevtil.site']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': '8NIKr1xh#mWG3%wbQX-<7}.RJ!w{],$,',
        'HOST': 'ls-fed61a92734f9c9a4c04b9d59c6b674e9571a55e.cygybgxia1m9.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}