# Generated by Django 4.0.4 on 2022-04-16 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExtAPIs', '0012_alter_fibonaccimodel_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoseriesmodel',
            name='start',
            field=models.FloatField(default=0),
        ),
    ]
