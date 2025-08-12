from celery import shared_task
from django.utils import timezone

from habit.services import send_telegram_message

from habit.models import Habit


@shared_task
def reminder_to_follow_a_habit():
    """Отложенная задача, которая отправляет напоминание в tg"""
    message = "Пора выполнять привычку"
    today = timezone.now().today().time()
    habits = Habit.objects.all()
    for habit in habits:
        tg_id = habit.owner.tg_chat_id
        time = habit.time
        if today >= time:
            send_telegram_message(tg_id, message)
