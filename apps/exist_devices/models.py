from django.db import models
from django.utils.translation import gettext_lazy as _


class Device(models.Model):
    id = models.CharField(
        max_length=11,
        primary_key=True,
        verbose_name=_('ID')
    )

    added_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Added at')
    )

    is_active = models.BooleanField(
        default=False,
        verbose_name=_('Is active'),
        blank=True
    )

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = _('Device')
        verbose_name_plural = _('Devices')
