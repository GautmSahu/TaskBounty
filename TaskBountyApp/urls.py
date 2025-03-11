from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppViewSet, UserPointsViewSet

router = DefaultRouter()
router.register(r'apps', AppViewSet)
router.register(r'points', UserPointsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
