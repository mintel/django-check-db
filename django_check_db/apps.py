try:
    from django.apps import AppConfig
except ImportError:
    pass
else:
    class CheckDbConfig(AppConfig):
        name = 'django_check_db'
