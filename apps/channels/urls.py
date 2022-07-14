from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.master_home_page, name='master_dashboard'),
    path('detail/<str:device_id>/', views.device_detail, name='device_detail'),
    path('detail/<str:device_id>/delete-channel-device/', views.delete_channel_device, name='delete_channel_device'),
    path(
        'detail/<str:device_id>/edit-channel-device/',
        views.edit_channel_device_data,
        name='edit_channel_device_data'),
    path('add-new-device/', views.add_new_device, name='add_new_device'),
]
