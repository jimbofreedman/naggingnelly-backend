from rest_framework import serializers

from .models import Context, TodoItem


class ContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Context
        fields = ['id', 'name', ]


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['id', 'title', 'start', 'due', 'completed', 'order', 'urgency',
                  'time_estimate', 'contexts', 'dependencies', ]
