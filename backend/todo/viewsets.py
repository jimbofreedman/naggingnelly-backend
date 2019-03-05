from rest_framework import viewsets
from .serializers import ContextSerializer, TodoItemSerializer
from .models import Context, TodoItem


class ContextViewSet(viewsets.ModelViewSet):
    serializer_class = ContextSerializer

    def get_queryset(self):
        return Context.objects.all()


class TodoItemViewSet(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer

    def get_queryset(self):
        return TodoItem.objects.all()
