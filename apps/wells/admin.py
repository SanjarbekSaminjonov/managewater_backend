from django.contrib import admin
from .models import WellDevice, WellDeviceMessage
from .forms import WellDeviceAdminForm


class WellDeviceAdmin(admin.ModelAdmin):
    form = WellDeviceAdminForm
    list_display = ('name', 'device', 'user', 'phone_number')
    search_fields = ('name', 'phone_number')


class WellDeviceMessageAdmin(admin.ModelAdmin):
    list_display = ('device', 'h', 'mineral', 'temperature', 'bat', 'is_charging', 'net', 'created_at')


admin.site.register(WellDevice, WellDeviceAdmin)
admin.site.register(WellDeviceMessage, WellDeviceMessageAdmin)
