from django.urls import path
from .views import receive_well_message


urlpatterns = [
    path('messages/new/', receive_well_message),
]
