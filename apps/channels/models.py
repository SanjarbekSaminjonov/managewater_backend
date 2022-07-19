from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from apps.exist_devices.models import Device


class ChannelDevice(models.Model):
    device = models.OneToOneField(
        to=Device,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name=_('Device')
    )

    ministry_id = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_('Ministry ID')
    )

    permission_to_send = models.BooleanField(
        default=False,
        verbose_name=_('Permission to send data')
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

    full_height = models.DecimalField(
        default=0.0,
        max_digits=8,
        decimal_places=2,
        verbose_name=_('Full height (sm)')
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
    device = models.ForeignKey(
        to=ChannelDevice,
        on_delete=models.CASCADE,
        verbose_name=_('Device')
    )

    tens = models.IntegerField(
        default=0,
        verbose_name=_('Tens')
                               )
    zero = models.FloatField(default=0, verbose_name='0')
    one = models.FloatField(default=0, verbose_name='1')
    two = models.FloatField(default=0, verbose_name='2')
    three = models.FloatField(default=0, verbose_name='3')
    four = models.FloatField(default=0, verbose_name='4')
    five = models.FloatField(default=0, verbose_name='5')
    six = models.FloatField(default=0, verbose_name='6')
    seven = models.FloatField(default=0, verbose_name='7')
    eight = models.FloatField(default=0, verbose_name='8')
    nine = models.FloatField(default=0, verbose_name='9')

    def __str__(self):
        return f'{self.id} / {self.device} / {self.tens}'

    def get_value(self, ones):
        match_values = {
            0: self.zero,
            1: self.one,
            2: self.two,
            3: self.three,
            4: self.four,
            5: self.five,
            6: self.six,
            7: self.seven,
            8: self.eight,
            9: self.nine
        }
        return match_values.get(ones)


class ChannelMessage(models.Model):
    device = models.ForeignKey(
        to=ChannelDevice,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name=_('Channel device')
    )

    h = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name=_('From device to water (sm)')
    )

    water_volume = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name=_('Volume of water (cubic meters/sec)')
    )

    bat = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name=_('Battery power (volt)')
    )

    is_charging = models.BooleanField(
        blank=True,
        null=True,
        verbose_name=_('Is charging')
    )

    net = models.SmallIntegerField(
        verbose_name=_('Network quality')
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Added time')
    )

    def __str__(self):
        return self.device.name

    class Meta:
        verbose_name = _('Channel message')
        verbose_name_plural = _('Channels messages')
