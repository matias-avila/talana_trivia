import os
from .Base import *

DEBUG = True
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
SECRET_KEY_JWT = os.environ.get('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(',')
CORS_ALLOWED_ORIGINS = os.environ.get('DJANGO_CORS').split(',')

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DJANGO_SQL_SERVER_ENGINE'),
        'NAME': os.environ.get('DJANGO_SQL_SERVER_BASEDATOS'),
        'USER': os.environ.get('DJANGO_SQL_SERVER_USUARIO'),
        'PASSWORD': os.environ.get('DJANGO_SQL_SERVER_PASSWORD'),
        'HOST': os.environ.get('DJANGO_SQL_SERVER_HOST'),
        'PORT': '',
        'COLLATION': os.environ.get('DJANGO_SQL_SERVER_COLLATION'),
        'OPTIONS':{
            'driver': os.environ.get('DJANGO_SQL_SERVER_DRIVER'),
            'collation': os.environ.get('DJANGO_SQL_SERVER_COLLATION'),
        },
        'TEST': {
             'NAME': os.environ.get('DJANGO_SQL_SERVER_BASEDATOS'),
        }
    }
}