from django.contrib import admin
from .models import WellDevice, WellDeviceMessage
from ..exist_devices.models import Device


class WellDeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'device', 'user', 'phone_number')
    search_fields = ('name', 'phone_number')

    obj_id = None

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.obj_id = obj.device.id
        return super(WellDeviceAdmin, self).get_form(request, obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'device':
            if self.obj_id:
                kwargs['queryset'] = Device.objects.filter(type='well')
                self.obj_id = None
            else:
                kwargs['queryset'] = Device.objects.filter(type='well').filter(is_active=False)
        return super(WellDeviceAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class WellDeviceMessageAdmin(admin.ModelAdmin):
    list_display = ('device', 'is_sent', 'h', 'mineral', 'temperature', 'bat', 'is_charging', 'net', 'created_at')


admin.site.register(WellDevice, WellDeviceAdmin)
admin.site.register(WellDeviceMessage, WellDeviceMessageAdmin)
