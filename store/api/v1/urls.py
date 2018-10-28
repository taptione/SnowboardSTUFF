from django.urls import path, include
from rest_framework import routers

from store.api.v1.user import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
