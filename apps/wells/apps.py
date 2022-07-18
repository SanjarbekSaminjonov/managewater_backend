from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WellsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.wells'
    verbose_name = _('Wells data')
