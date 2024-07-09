from django.apps import AppConfig # type: ignore
from django.utils.translation import gettext_lazy as _ # type: ignore

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    # name = "google_auth.users"
    verbose_name = _("Users")
    
    def ready(self) -> None:
        try:
            import users.signals
        except ImportError:
            pass
