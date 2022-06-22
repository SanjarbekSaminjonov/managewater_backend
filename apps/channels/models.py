from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from apps.exist_devices.models import Device


# Create your models here.

class ChannelDevice(models.Model):
    device = models.OneToOneField(
        to=Device,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name=_('Device')
    )

    name = models.CharField(
        max_length=100,
        verbose_name=_('Name')
    )

    belong_to = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='channeldevices',
        verbose_name=_('Belong to')
    )

    phone_number = models.CharField(
        max_length=13,
        verbose_name=_('Phone number')
    )

    height = models.DecimalField(
        default=0.0,
        max_digits=8,
        decimal_places=2,
        verbose_name=_('Height of device (sm)')
    )

    height_conf = models.IntegerField(
        default=0,
        blank=True,
        verbose_name=_('Height conf (sm)')
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name=_('Latitude of location'),
        blank=True,
        null=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name=_('Longitude of location'),
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.device.id} - {self.name}'

    class Meta:
        verbose_name = 'Channel device'
        verbose_name_plural = 'Channel devices'
