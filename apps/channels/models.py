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

    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.SET_NULL,
        related_name='channeldevices',
        null=True,
        blank=True,
        verbose_name=_('Belong to')
    )

    master = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.SET_NULL,
        related_name='channel_devices',
        null=True,
        blank=True,
        verbose_name=_('Master')
    )

    phone_number = models.CharField(
        max_length=13,
        verbose_name=_('Phone number')
    )

    height = models.DecimalField(
        default=0.0,
        max_digits=8,
        decimal_places=2,
        verbose_name=_('Height of water (sm)')
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
        return f'{self.device.id}'

    def save(self, *args, **kwargs):
        self.device.is_active = True
        self.device.save()
        super(ChannelDevice, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.device.is_active = False
        self.device.save()
        super(ChannelDevice, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = _('Channel device')
        verbose_name_plural = _('Channel devices')


class ChannelDeviceVolumeTable(models.Model):
    device = models.ForeignKey(to=ChannelDevice, on_delete=models.CASCADE)
    tens = models.IntegerField()
    ones = models.IntegerField()
    value = models.FloatField()

    def __str__(self):
        return f'{self.id} / {self.device} / {self.tens + self.ones} / {self.value}'


class ChannelMessage(models.Model):
    channel_device = models.ForeignKey(
        to=ChannelDevice,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name=_('Channel device')
    )

    h1 = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name=_('H1 (sm)')
    )

    h2 = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name=_('H2 (sm)')
    )

    w1 = models.IntegerField(
        verbose_name=_('W1 (liter/sec)')
    )

    w2 = models.IntegerField(
        verbose_name=_('W2 (cubic meters/hour)')
    )

    vol = models.BigIntegerField(
        verbose_name=_('Total amount of water')
    )

    bat = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name=_('Battery power (volt)')
    )

    net = models.SmallIntegerField(
        verbose_name=_('Network quality')
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Added time')
    )

    def __str__(self):
        return self.channel_device.name

    class Meta:
        verbose_name = _('Channel message')
        verbose_name_plural = _('Channels messages')
