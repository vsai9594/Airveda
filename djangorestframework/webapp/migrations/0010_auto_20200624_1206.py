# Generated by Django 3.0.6 on 2020-06-24 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20200624_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humidity',
            name='humidity',
            field=models.CharField(max_length=20),
        ),
    ]
