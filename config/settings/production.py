from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'main',
        'USER':'postgres',
        'PASSWORD':'Kick101Ass#@',
        'HOST': 'localhost'
    }
}