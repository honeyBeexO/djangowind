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

