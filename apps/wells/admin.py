from django.contrib import admin
from .models import WellDevice
from .forms import WellDeviceAdminForm


class WellDeviceAdmin(admin.ModelAdmin):
    form = WellDeviceAdminForm
    list_display = ('name', 'device', 'user', 'phone_number')
    search_fields = ('name', 'phone_number')


admin.site.register(WellDevice, WellDeviceAdmin)
