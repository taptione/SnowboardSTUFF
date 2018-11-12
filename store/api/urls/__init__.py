from django.urls import path, include

urlpatterns = [
    path('v1/admin/', include('store.api.urls.admin')),
    path('v1/', include('store.api.urls.client')),
]
