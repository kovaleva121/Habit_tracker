from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """Класс для отображения атрибутов в панели админки"""

    list_display = ("id", "action")
