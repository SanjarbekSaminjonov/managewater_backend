# Generated by Django 4.0.6 on 2022-07-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0007_remove_channeldevicevolumetable_ones_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='channeldevicevolumetable',
            name='_7',
            field=models.FloatField(default=0),
        ),
    ]
