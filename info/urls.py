from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CreateUserApi, AuthTokenApi, CreateInfoApi, InfoViewApi, ManageUserViewApi

router = DefaultRouter()
router.register('info', InfoViewApi)

urlpatterns = [
    path("", include(router.urls)),
    path('create/', CreateUserApi.as_view(), name='create'),
    path('create_info/', CreateInfoApi.as_view(), name='create_info'),
    path('token/', AuthTokenApi.as_view(), name='token'),
    # path('info', InfoViewApi.as_view(), name='info'),
    path('me/', ManageUserViewApi.as_view(), name='me'),
]
