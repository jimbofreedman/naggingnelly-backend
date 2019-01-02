from django.urls import path

from .views import index, complete, cancel, fail

app_name = "todo"
urlpatterns = [
    path(r'complete/<int:item_id>/', view=complete, name="complete"),
    path(r'cancel/<int:item_id>/', view=cancel, name="cancel"),
    path(r'fail/<int:item_id>/', view=fail, name="fail"),
    path('', view=index, name="index"),
]
