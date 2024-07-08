from config.env import env

CELERY_BROKER_URL = env('CELERY_BROKER_URL')

# Let's imagine we are using 'djang-celery-results' an extension for stroing 
# Celery Task resuls in the DB CELERY_RESULT_BACKEND = 'django-db'

CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND')
CELERY_RESULT_EXTENDED = env.bool('CELERY_RESULT_EXTENDED',default=False)