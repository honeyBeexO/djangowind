from django.conf import settings # type: ignore
from config.env import env

def settings_context(_request):
    """Settings available by default to the templates context."""
    # Note: we intentionally do NOT expose the entire settings
    # to prevent accidental leaking of sensitive information
    return {"DEBUG": settings.DEBUG}


def google_client_id(request):
    return {
        'GOOGLE_CLIENT_ID': env('GOOGLE_CLIENT_ID')
    }
