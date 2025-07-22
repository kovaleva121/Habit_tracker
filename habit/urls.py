from django.urls import path
from habit.apps import HabitConfig

from habit.views import HabitCreateApiView, HabitRetrieveApiView, HabitUpdateApiView, HabitDestroyApiView, \
    HabitListApiView, HabitPublicListApiView

app_name = HabitConfig.name

urlpatterns = [
    path('list/', HabitListApiView.as_view(), name='habit_list'),
    path('<int:pk>/detail/', HabitRetrieveApiView.as_view(), name='habit_retrieve'),
    path('create/', HabitCreateApiView.as_view(), name='habit_create'),
    path('<int:pk>/update/', HabitUpdateApiView.as_view(), name='habit_update'),
    path('<int:pk>/delete/', HabitDestroyApiView.as_view(), name='habit_delete'),
    path('public/', HabitPublicListApiView.as_view(), name='public_list'),

]
