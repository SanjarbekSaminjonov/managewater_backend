from django.db import models
from django.utils.translation import gettext_lazy as _


class MinistryChannelLink(models.Model):
    link = models.CharField(
        max_length=255,
        verbose_name=_('Full path to send json')
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated date and time')
    )

    added_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Added date and time')
    )

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = _('Ministry channel link')
        verbose_name_plural = _('Ministry channel links')


class MinistryWellLink(models.Model):
    link = models.CharField(
        max_length=255,
        verbose_name=_('Full path to send json')
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated date and time')
    )

    added_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Added date and time')
    )

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = _('Ministry well link')
        verbose_name_plural = _('Ministry well links')
