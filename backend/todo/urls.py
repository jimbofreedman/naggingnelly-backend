from django.urls import path, include
# from django.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import index, complete, cancel, fail
from .viewsets import TodoItemViewSet

app_name = "todo"

router = DefaultRouter()
router.register(r'todo_items', TodoItemViewSet, base_name='todo_items')

urlpatterns = [
    path(r'complete/<int:item_id>/', view=complete, name="complete"),
    path(r'cancel/<int:item_id>/', view=cancel, name="cancel"),
    path(r'fail/<int:item_id>/', view=fail, name="fail"),
    path('', view=index, name="index"),
    path(r'api/', include(router.urls)),
]
