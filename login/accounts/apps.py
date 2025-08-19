# accounts/apps.py
from django.apps import AppConfig  # required

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        # import signals if you use them
        try:
            import accounts.signals  # noqa: F401
        except Exception:
            pass
