from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ConnectionShiftViewApi

router = DefaultRouter()
router.register("", ConnectionShiftViewApi)

urlpatterns = [
    path("", include(router.urls)),
]
