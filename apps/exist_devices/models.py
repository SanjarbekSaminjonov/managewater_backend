from django.db import models
from django.utils.translation import gettext_lazy as _


class Device(models.Model):
    DEVICE_TYPE_CHOICES = (
        ('channel', _('Water Channel')),
        ('well', _('Water Well')),
    )

    id = models.CharField(
        max_length=11,
        primary_key=True,
        verbose_name=_('ID')
    )

    type = models.CharField(
        max_length=20,
        choices=DEVICE_TYPE_CHOICES,
        verbose_name=_('Type of device')
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
