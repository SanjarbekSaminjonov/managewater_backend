from django.urls import path

from .views import signup_user

urlpatterns = [
    path('singup/', signup_user)
]
