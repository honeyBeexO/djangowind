from django.apps import AppConfig # type: ignore


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
    def ready(self) -> None:
        try:
            import users.signals
        except ImportError:
            pass
