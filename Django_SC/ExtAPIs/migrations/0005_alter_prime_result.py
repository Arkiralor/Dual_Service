# Generated by Django 4.0.4 on 2022-04-14 16:51

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExtAPIs', '0004_alter_prime_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prime',
            name='result',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=8191),
        ),
    ]