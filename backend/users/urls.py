from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import UserViewSet

app_name = "backend.users"

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')

urlpatterns = [
    path("", include(router.urls)),
]
