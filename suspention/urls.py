from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PermanentSuspentionApiView, TemporarySuspentionApiView

router = DefaultRouter()
router.register('permanent', PermanentSuspentionApiView)
router.register('temporary', TemporarySuspentionApiView)

urlpatterns = [
    path('', include(router.urls)),
]
