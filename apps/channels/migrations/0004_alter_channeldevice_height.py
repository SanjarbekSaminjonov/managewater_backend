# Generated by Django 4.0.5 on 2022-07-13 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0003_channeldevice_master_alter_channeldevice_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channeldevice',
            name='height',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Height of water (sm)'),
        ),
    ]
