from django.urls import path, include


urlpatterns = [
    path('', include('apps.home.urls')),
    path('auth/', include('apps.accounts.urls')),
    path('channels/masters/', include('apps.channels.urls')),
]
