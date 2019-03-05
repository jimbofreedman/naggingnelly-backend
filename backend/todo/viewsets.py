from rest_framework import viewsets
from .serializers import TodoItemSerializer
from .models import TodoItem


class TodoItemViewSet(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return TodoItem.objects.all()
