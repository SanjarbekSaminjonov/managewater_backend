from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.exist_devices.models import Device


class WellDevice(models.Model):
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

    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.SET_NULL,
        related_name='welldevices',
        null=True,
        blank=True,
        verbose_name=_('Belong to')
    )

    phone_number = models.CharField(
        max_length=13,
        verbose_name=_('Phone number')
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
        return f'{self.name} - {self.device}'

    def save(self, *args, **kwargs):
        self.device.is_active = True
        self.device.save()
        super(WellDevice, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.device.is_active = False
        self.device.save()
        super(WellDevice, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = _('Well device')
        verbose_name_plural = _('Wells devices')


class WellDeviceMessage(models.Model):
    device = models.ForeignKey(
        to=WellDevice,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name=_('Well device')
    )

    h = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Water height (sm)')
    )

    mineral = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name=_('Mineral (gramm/liter)')
    )

    temperature = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name=_('Temperature (Celsius)')
    )

    bat = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name=_('Battery power (volt)')
    )

    is_charging = models.BooleanField(
        blank=True,
        null=True,
        verbose_name=_('Is charging')
    )

    net = models.SmallIntegerField(
        blank=True,
        null=True,
        verbose_name=_('Network quality')
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Added time')
    )

    def __str__(self):
        return self.device.name

    class Meta:
        verbose_name = _('Well message')
        verbose_name_plural = _('Wells messages')
