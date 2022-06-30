from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
from apps.channels.models import ChannelDevice


class ChannelWatcher(models.Model):
    device = models.ForeignKey(
        to=ChannelDevice,
        on_delete=models.CASCADE,
        verbose_name=_('Device')
    )

    watcher = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_('Watcher')
    )

    connected_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Connected at')
    )

    def __str__(self):
        return f'{self.device.name} - {self.watcher.username}'

    class Meta:
        verbose_name = _('Channel watcher')
        verbose_name_plural = _('Channel watchers')
