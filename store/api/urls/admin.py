from django.urls import path, include
from rest_framework import routers
from store.api.controllers.user.admin.v1 import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
