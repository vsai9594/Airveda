# Generated by Django 3.0.6 on 2020-06-24 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_auto_20200624_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='devices',
            name='uid',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
