from django.contrib import admin
from .models import Device

# Register your models here.


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'added_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('id',)
    ordering = ('-added_at',)
    date_hierarchy = 'added_at'


admin.site.register(Device, DeviceAdmin)
