from django.contrib import admin

from .models import ChannelDevice, ChannelMessage, ChannelDeviceVolumeTable


# Register your models here.


class ChannelDeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'device', 'user', 'phone_number', 'height', 'height_conf')
    search_fields = ('name', 'phone_number')


class ChannelMessageAdmin(admin.ModelAdmin):
    list_display = ('channel_device', 'h1', 'h2', 'w1', 'w2', 'vol', 'created_at')
    ordering = ('-created_at',)


class ChannelDeviceVolumeTableAdmin(admin.ModelAdmin):
    list_display = (
        'device', 'tens', 'zero', 'one', 'two', 'three',
        'four', 'five', 'six', 'seven', 'eight', 'nine'
    )
    ordering = ('device', 'tens')


admin.site.register(ChannelDevice, ChannelDeviceAdmin)
admin.site.register(ChannelMessage, ChannelMessageAdmin)
admin.site.register(ChannelDeviceVolumeTable, ChannelDeviceVolumeTableAdmin)
