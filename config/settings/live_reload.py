from config.env import BASE_DIR, env
#LIVERELOAD_SERVER_PORT = 8080

# Explicitly specify the directories to watch
LIVERELOAD_WATCH_PATHS = [
    str(BASE_DIR / 'templates'),
    str(BASE_DIR / 'static'),
    str(BASE_DIR / 'users/static'),
    str(BASE_DIR / 'users/templates/users/'),
]

#LIVE_RELOAD_MIDDLEWARE ='livereload.middleware.LiveReloadScript'