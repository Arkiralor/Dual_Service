# Generated by Django 4.0.4 on 2022-04-16 15:58

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExtAPIs', '0011_alter_arithseriesmodel_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonaccimodel',
            name='result',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=8191),
        ),
    ]