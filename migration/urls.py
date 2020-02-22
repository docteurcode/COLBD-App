from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MigrateApiView


router = DefaultRouter()
router.register("", MigrateApiView)

urlpatterns = [
    path("", include(router.urls)),
]
