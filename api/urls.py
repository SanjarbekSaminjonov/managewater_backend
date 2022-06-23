from django.urls import path, include

urlpatterns = [
    path('auth/', include('api.auth.urls')),
    path('channels/', include('api.channels.urls')),
]
