# Generated by Django 3.0.6 on 2020-06-24 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20200624_1206'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Humidity',
            new_name='HumidityReading',
        ),
        migrations.RenameModel(
            old_name='Temperature',
            new_name='TemperatureReading',
        ),
    ]
