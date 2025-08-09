from django.apps import AppConfig


class HabitConfig(AppConfig):
    """Конфигурационное имя приложения"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "habit"
