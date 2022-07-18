# Generated by Django 4.0.6 on 2022-07-18 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0002_alter_welldevice_options_welldevicemessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='welldevicemessage',
            name='bat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Battery power (volt)'),
        ),
        migrations.AlterField(
            model_name='welldevicemessage',
            name='net',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Network quality'),
        ),
    ]
