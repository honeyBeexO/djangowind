from django.conf import settings # type: ignore
from config.env import env
from config.env import BASE_DIR, env
import os

env.read_env(os.path.join(BASE_DIR, '.env'))

def settings_context(_request):
    """Settings available by default to the templates context."""
    # Note: we intentionally do NOT expose the entire settings
    # to prevent accidental leaking of sensitive information
    return {"DEBUG": settings.DEBUG}


def google_client_id(request):
    return {
        'GOOGLE_CLIENT_ID': '932595278480-8ij7icfa3ifucc9djup4ciijgm7cu90q.apps.googleusercontent.com' #env('GOOGLE_CLIENT_ID')
    }

def google_maps_api_key(request):
    print(f'Maps api key: {env('GOOGLE_MAPS_API_KEY')}')
    return {
        'GOOGLE_MAPS_API_KEY': env('GOOGLE_MAPS_API_KEY')
    }