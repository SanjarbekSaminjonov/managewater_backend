from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.master_home_page, name='master_dashboard')
]
