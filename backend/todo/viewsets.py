from rest_framework import viewsets, permissions
from .serializers import ContextSerializer, TodoItemSerializer
from .models import Context, TodoItem

class ContextViewSet(viewsets.ModelViewSet):
    serializer_class = ContextSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Context.objects.all()

class TodoItemViewSet(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TodoItem.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
