from .base import *
from config.env import env

DEBUG = env.bool('DJANGO_DEBUG',default=True)

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS',default=['127.0.0.1','localhost'])
# Check if this is the main process or a reloader subprocess
import os
if os.environ.get('RUN_MAIN') == 'true':
    print(f'--> DJANGO_ALLOWED_HOSTS: {ALLOWED_HOSTS}')

from config.settings.compressor import *
from config.settings.live_reload import *
from config.settings.stripe import *


CACHES = {
    "default":{
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}
 # Email settings: # https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_TIMEOUT = 5

 # General settings 
#MIDDLEWARE+=[LIVE_RELOAD_MIDDLEWARE]    #'debug_toolbar.middleware.DebugToolbarMiddleware'] # live reloading and django toolbar
INTERNAL_IPS = ["127.0.0.1","0.0.0.0"]  # For the django tool bar


# Admin settings
# # Django Admin URL.
# ADMIN_URL = "admin/"
# # https://docs.djangoproject.com/en/dev/ref/settings/#admins
# ADMINS = [("""Leon Wei""", "leon@instamentor.com")]
# # https://docs.djangoproject.com/en/dev/ref/settings/#managers
# MANAGERS = ADMINS
