# Generated by Django 4.0.6 on 2022-07-19 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exist_devices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WellDevice',
            fields=[
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='exist_devices.device', verbose_name='Device')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Phone number')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Latitude of location')),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Longitude of location')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='welldevices', to=settings.AUTH_USER_MODEL, verbose_name='Belong to')),
            ],
            options={
                'verbose_name': 'Well device',
                'verbose_name_plural': 'Wells devices',
            },
        ),
        migrations.CreateModel(
            name='WellMovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Latitude of location')),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Longitude of location')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Added time')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wells.welldevice', verbose_name='Device')),
            ],
            options={
                'verbose_name': 'Well movement message',
                'verbose_name_plural': 'Wells movement messages',
            },
        ),
        migrations.CreateModel(
            name='WellDeviceMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_sent', models.BooleanField(default=False, verbose_name='Is sent')),
                ('h', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Water height (sm)')),
                ('mineral', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Mineral (gramm/liter)')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Temperature (Celsius)')),
                ('bat', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Battery power (volt)')),
                ('is_charging', models.BooleanField(blank=True, null=True, verbose_name='Is charging')),
                ('net', models.SmallIntegerField(blank=True, null=True, verbose_name='Network quality')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Added time')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='wells.welldevice', verbose_name='Well device')),
            ],
            options={
                'verbose_name': 'Well message',
                'verbose_name_plural': 'Wells messages',
            },
        ),
    ]
