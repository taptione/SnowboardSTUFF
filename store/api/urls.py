from django.urls import path, include

urlpatterns = [
    path('v1/', include('store.api.v1.urls')),
]
