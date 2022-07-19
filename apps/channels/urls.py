from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.master_home_page, name='master_dashboard'),
    path('detail/<str:device_id>/', views.device_detail, name='device_detail'),
    path('detail/<str:device_id>/delete-channel-device/', views.delete_channel_device, name='delete_channel_device'),
    path(
        'detail/<str:device_id>/edit-channel-device/',
        views.edit_channel_device_data,
        name='edit_channel_device_data'
    ),
    path(
        'detail/<str:device_id>/volume-table/',
        views.volume_table,
        name='volume_table'
    ),
    path(
        'detail/<str:device_id>/last-messages/',
        views.last_messages,
        name='last_messages'
    ),
    path(
        'detail/<str:device_id>/new/',
        views.add_new_row_for_volume_table,
        name='add_new_row_for_volume_table'
    ),
    path(
        'detail/<int:row_id>/edit/',
        views.edit_new_row_for_volume_table,
        name='edit_new_row_for_volume_table'
    ),
    path(
        'detail/<int:row_id>/delete/',
        views.delete_new_row_for_volume_table,
        name='delete_new_row_for_volume_table'
    ),
    path('add-new-device/', views.add_new_device, name='add_new_device'),
]
