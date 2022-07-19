from django.contrib import admin
from .models import ChannelDevice, ChannelMessage, ChannelDeviceVolumeTable
from .forms import ChannelDeviceAdminForm


class ChannelDeviceAdmin(admin.ModelAdmin):
    form = ChannelDeviceAdminForm
    list_display = (
        'name', 'device', 'ministry_id', 'permission_to_send',
        'user', 'phone_number', 'full_height', 'height', 'height_conf'
    )
    search_fields = ('name', 'phone_number', 'ministry_id')


class ChannelMessageAdmin(admin.ModelAdmin):
    list_display = ('device', 'h', 'water_volume', 'bat', 'is_charging', 'net', 'created_at')
    list_filter = ('device',)
    ordering = ('-created_at',)


class ChannelDeviceVolumeTableAdmin(admin.ModelAdmin):
    list_display = (
        'device', 'tens', 'zero', 'one', 'two', 'three',
        'four', 'five', 'six', 'seven', 'eight', 'nine'
    )
    list_filter = ('device',)
    ordering = ('device', 'tens')


admin.site.register(ChannelDevice, ChannelDeviceAdmin)
admin.site.register(ChannelMessage, ChannelMessageAdmin)
admin.site.register(ChannelDeviceVolumeTable, ChannelDeviceVolumeTableAdmin)
