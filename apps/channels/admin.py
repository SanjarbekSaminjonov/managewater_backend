from django.contrib import admin
from .models import ChannelDevice

# Register your models here.


class ChannelDeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'device', 'belong_to', 'phone_number', 'height', 'height_conf')
    search_fields = ('name', 'phone_number')


admin.site.register(ChannelDevice, ChannelDeviceAdmin)
