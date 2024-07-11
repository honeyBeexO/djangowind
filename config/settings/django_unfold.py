#https://github.com/unfoldadmin/django-unfold?tab=readme-ov-file#installation
NFOLD_APPS = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    #"unfold.contrib.guardian",  # optional, if django-guardian package is used
    #"unfold.contrib.simple_history",  # optional, if django-simple-history package is used
]