# Generated by Django 4.0.4 on 2022-04-16 15:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExtAPIs', '0010_alter_geoseriesmodel_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arithseriesmodel',
            name='result',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=8191),
        ),
    ]
