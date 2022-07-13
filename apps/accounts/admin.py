from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from .models import User
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(UserAdminBase):
    model = User
    add_form = UserCreationForm
    form = UserChangeForm

    list_display = (
        'username', 'first_name', 'last_name',
        'region', 'city', 'org_name', 'telegram_id', 'is_master'
    )

    search_fields = (
        'username', 'first_name', 'last_name',
        'region', 'city', 'org_name', 'telegram_id',
    )

    fieldsets = (
        *UserAdminBase.fieldsets,
        (
            _('Additional information'),
            {
                'fields': (
                    'telegram_id',
                    'region',
                    'city',
                    'org_name',
                    'is_master'
                )
            }
        )
    )


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

admin.site.site_header = _("Carwon Group Admin")
admin.site.site_title = _("Carwon Admin Portal")
admin.site.index_title = _("Welcome to Manage Water Administration")
