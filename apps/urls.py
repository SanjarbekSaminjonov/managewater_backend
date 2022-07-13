from django.urls import path, include


urlpatterns = [
    path('auth/', include('apps.accounts.urls')),
    path('channels/', include('apps.channels.urls')),
]
