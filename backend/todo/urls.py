from django.urls import path

from .views import index, complete

app_name = "todo"
urlpatterns = [
    path(r'complete/<int:item_id>/', view=complete, name="complete"),
    path('', view=index, name="index"),
]
