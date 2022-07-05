# Generated by Django 4.0.5 on 2022-06-30 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('channels', '0002_alter_channeldevice_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelWatcher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connected_at', models.DateTimeField(auto_now_add=True, verbose_name='Connected at')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channels.channeldevice', verbose_name='Device')),
                ('watcher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Watcher')),
            ],
            options={
                'verbose_name': 'Channel watcher',
                'verbose_name_plural': 'Channel watchers',
            },
        ),
    ]
