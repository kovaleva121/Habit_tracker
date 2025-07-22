from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView

from habit.models import Habit
from habit.paginators import HabitPagination
from habit.permissions import IsOwner, IsPublicOrOwner
from habit.serializers import HabbitSerializer


class HabitCreateApiView(CreateAPIView):
    """Контроллер для создания привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabbitSerializer

    def perform_create(self, serializer):
        """Привязка пользователя при создании"""
        serializer.save(owner=self.request.user)


class HabitListApiView(ListAPIView):
    """Контроллер для просмотра списка привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabbitSerializer
    pagination_class = HabitPagination

    def get_queryset(self):
        """Отображение списка привычек только для создателя"""
        return Habit.objects.filter(owner=self.request.user)


class HabitPublicListApiView(ListAPIView):
    """Контроллер для просмотра списка публичных привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabbitSerializer
    pagination_class = HabitPagination

    def get_queryset(self):
        """Отображение списка только публичных привычек"""
        return Habit.objects.filter(is_public=True)


class HabitUpdateApiView(UpdateAPIView):
    """Контроллер для обновления привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = [IsOwner]


class HabitRetrieveApiView(RetrieveAPIView):
    """Контроллер для изменения привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = [IsPublicOrOwner]


class HabitDestroyApiView(DestroyAPIView):
    """Контроллер для удаления привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = [IsOwner]
