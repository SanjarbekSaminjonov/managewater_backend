from django.urls import path

from .views import signup_user

urlpatterns = [
    path('users/singup/', signup_user)
]
