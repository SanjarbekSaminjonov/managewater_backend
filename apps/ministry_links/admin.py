from django.contrib import admin
from .models import MinistryChannelLink, MinistryWellLink


class MinistryChannelLinkAdmin(admin.ModelAdmin):
    list_display = ('link', 'updated_at', 'added_at')


class MinistryWellLinkAdmin(admin.ModelAdmin):
    list_display = ('link', 'updated_at', 'added_at')


admin.site.register(MinistryChannelLink, MinistryChannelLinkAdmin)
admin.site.register(MinistryWellLink, MinistryWellLinkAdmin)
