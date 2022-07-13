# Generated by Django 4.0.5 on 2022-07-13 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('channels', '0002_alter_channeldevice_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='channeldevice',
            name='master',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel_devices', to=settings.AUTH_USER_MODEL, verbose_name='Master'),
        ),
        migrations.AlterField(
            model_name='channeldevice',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channeldevices', to=settings.AUTH_USER_MODEL, verbose_name='Belong to'),
        ),
    ]