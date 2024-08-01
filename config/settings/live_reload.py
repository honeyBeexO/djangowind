from config.env import BASE_DIR, env
#LIVERELOAD_SERVER_PORT = 8080
#'livereload', #'django_extensions',

# Explicitly specify the directories to watch
LIVERELOAD_WATCH_PATHS = [
    str(BASE_DIR / 'templates'),
    str(BASE_DIR / 'static'),
    str(BASE_DIR / 'users/static'),
    str(BASE_DIR / 'users/templates/users/'),
    str(BASE_DIR / 'templates/account/'),
    str(BASE_DIR / 'templates/config/'),
    str(BASE_DIR / 'templates/forms/'),
    str(BASE_DIR / 'templates/forms/sections/'),
    str(BASE_DIR / 'templates/sections/'),
    str(BASE_DIR / 'templates/sections/buttons/'),
    str(BASE_DIR / 'templates/stripe/'),
    str(BASE_DIR / 'templates/tests/'),
    str(BASE_DIR / 'templates/utils/'),

]

#LIVE_RELOAD_MIDDLEWARE ='livereload.middleware.LiveReloadScript'