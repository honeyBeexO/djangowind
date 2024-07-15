from config.env import BASE_DIR, env
import os

env.read_env(os.path.join(BASE_DIR, '.env'))

# `allauth` specific authentication methods, such as login by email
ALL_AUTH_AUTHENTICATION_BACKENDS = 'allauth.account.auth_backends.AuthenticationBackend'
ALL_AUTH_MIDDLEWARE = "allauth.account.middleware.AccountMiddleware"

ALL_AUTH_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = "email"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_VERIFICATION = "none"#"mandatory"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ADAPTER = "users.adapters.AccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_ADAPTER = "users.adapters.SocialAccountAdapter"

ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "accounts.CustomUser"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "accounts:redirect"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "account_login"
LOGIN_REDIRECT_URL = 'users:redirect'
LOGOUT_REDIRECT_URL = '/'

# configure django to run ssl

SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SITE_ID = 1


# Your stuff...
# ------------------------------------------------------------------------------
# Disable conformation step
SOCIALACCOUNT_LOGIN_ON_GET=True

SECURE_REFERRER_POLICY= "strict-origin-when-cross-origin"

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'APP': {
            'client_id': env('GOOGLE_CLIENT_ID'),
            'secret': env('GOOGLE_SECRET_KEY'),
            'key': '',
        },
        'OAUTH_PKCE_ENABLED': True,
        'FETCH_USERINFO': True,
        'sites': [1,2], # IDs of example.com and localhost:8000
    }
}


# Add this to the allauth settings in settings.py
ACCOUNT_FORMS = {
    'signup': 'users.forms.CustomSignupForm',
}