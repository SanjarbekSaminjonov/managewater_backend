from django.urls import path
from .views import receive_channel_message


urlpatterns = [
    path('messages/new/', receive_channel_message)
]
