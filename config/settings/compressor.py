from config.env import BASE_DIR, env
""" Django compressor configuration """
COMPRESS_ROOT = BASE_DIR / 'static'
 
COMPRESS_ENABLED = True
 
STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)
LIVE_RELOAD_MIDDLEWARE = 'livereload.middleware.LiveReloadScript'