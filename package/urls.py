from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PackageApiView, PackageOfferApiView

router = DefaultRouter()
router.register("package", PackageApiView)
router.register("offer", PackageOfferApiView)


urlpatterns = [
    path("", include(router.urls)),
]
