from django.contrib import admin
from .models import ChannelDevice, ChannelMessage, ChannelDeviceVolumeTable
from apps.exist_devices.models import Device


class ChannelDeviceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'device', 'ministry_id', 'permission_to_send',
        'user', 'phone_number', 'full_height', 'height', 'height_conf'
    )
    search_fields = ('name', 'phone_number', 'ministry_id')

    obj_id = None

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.obj_id = obj.device.id
        return super(ChannelDeviceAdmin, self).get_form(request, obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'device':
            if self.obj_id:
                kwargs['queryset'] = Device.objects.filter(type='channel')
            else:
                kwargs['queryset'] = Device.objects.filter(type='channel').filter(is_active=False)
        return super(ChannelDeviceAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class ChannelMessageAdmin(admin.ModelAdmin):
    list_display = ('device', 'is_sent', 'h', 'water_volume', 'bat', 'is_charging', 'net', 'created_at')
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
