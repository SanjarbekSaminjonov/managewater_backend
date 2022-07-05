from django.contrib import admin
from .models import ChannelWatcher

# Register your models here.


class ChannelWatcherAdmin(admin.ModelAdmin):
    list_display = ('device', 'watcher', 'connected_at', 'id')


admin.site.register(ChannelWatcher, ChannelWatcherAdmin)
