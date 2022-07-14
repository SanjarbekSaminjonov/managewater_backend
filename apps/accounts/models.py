from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_('Phone number'),
        error_messages={
            'unique': _("A user with that phone number already exists."),
        },
    )

    region = models.CharField(
        max_length=255,
        verbose_name=_('Region'),
        blank=True,
        null=True,
    )

    city = models.CharField(
        max_length=255,
        verbose_name=_('City'),
        blank=True,
        null=True,
    )

    org_name = models.CharField(
        max_length=500,
        verbose_name=_('Organization name'),
        blank=True,
        null=True,
    )

    telegram_id = models.CharField(
        max_length=255,
        verbose_name=_('Telegram ID'),
        blank=True,
        null=True,
    )

    is_master = models.BooleanField(
        default=False,
        verbose_name=_('Is channels_master')
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
