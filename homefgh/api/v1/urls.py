from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import DdfgssfgViewSet

router = DefaultRouter()
router.register("ddfgssfg", DdfgssfgViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
