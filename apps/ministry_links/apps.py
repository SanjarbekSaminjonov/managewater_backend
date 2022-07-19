from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MinistryLinksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.ministry_links'
    verbose_name = _('Ministry links')
