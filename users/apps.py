from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Конфигурационное имя приложения"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
