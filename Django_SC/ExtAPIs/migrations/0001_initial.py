# Generated by Django 4.0.4 on 2022-04-19 10:57

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectilePath2DModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_at', models.DateTimeField(auto_now=True)),
                ('function', models.CharField(max_length=256)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('launch_angle', models.FloatField(default=0)),
                ('launch_height', models.FloatField(default=0)),
                ('launch_velocity', models.FloatField(default=0)),
                ('result', django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), size=8191)),
                ('requested_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_projectile_2d_requester', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-requested_at'],
                'unique_together': {('function', 'launch_angle', 'launch_height', 'launch_velocity')},
            },
        ),
        migrations.CreateModel(
            name='PrimeFactorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_at', models.DateTimeField(auto_now=True)),
                ('function', models.CharField(max_length=256)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('query', models.IntegerField()),
                ('result', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=8191)),
                ('requested_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_prime_factor_requester', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-requested_at'],
                'unique_together': {('function', 'query')},
            },
        ),
        migrations.CreateModel(
            name='Prime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_at', models.DateTimeField(auto_now=True)),
                ('function', models.CharField(max_length=256)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('query', models.IntegerField()),
                ('result', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=8191)),
                ('requested_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_prime_requester', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-requested_at'],
                'unique_together': {('function', 'query')},
            },
        ),
        migrations.CreateModel(
            name='IntToBinaryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_at', models.DateTimeField(auto_now=True)),
                ('function', models.CharField(max_length=256)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('query', models.IntegerField()),
                ('result', models.CharField(max_length=256)),
                ('requested_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_inttobin_requester', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-requested_at'],
                'unique_together': {('function', 'result', 'query')},
            },
        ),
        migrations.CreateModel(
            name='GeoSeriesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_at', models.DateTimeField(auto_now=True)),
                ('function', models.CharField(max_length=256)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('start', models.FloatField(default=0)),
                ('terms', models.IntegerField(default=0)),
                ('cr', models.FloatField(default=0)),
                ('result', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=8191)),
                ('requested_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_geo_series_requester', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-requested_at'],
                'unique_together': {('function', 'start', 'terms', 'cr')},
            },
        ),
        migrations.CreateModel(
            name='FibonacciModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_at', models.DateTimeField(auto_now=True)),
                ('function', models.CharField(max_length=256)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('query', models.IntegerField()),
                ('result', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=8191)),
                ('requested_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_fibonacci_requester', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-requested_at'],
                'unique_together': {('function', 'query')},
            },
        ),
        migrations.CreateModel(
            name='Factor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_at', models.DateTimeField(auto_now=True)),
                ('function', models.CharField(max_length=256)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('query', models.IntegerField()),
                ('result', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=8191)),
                ('requested_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_factor_requester', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-requested_at'],
                'unique_together': {('function', 'query')},
            },
        ),
        migrations.CreateModel(
            name='BinaryToIntModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_at', models.DateTimeField(auto_now=True)),
                ('function', models.CharField(max_length=256)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('query', models.IntegerField()),
                ('result', models.CharField(max_length=256)),
                ('requested_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_bintoint_requester', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-requested_at'],
                'unique_together': {('function', 'result', 'query')},
            },
        ),
        migrations.CreateModel(
            name='ArithSeriesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_at', models.DateTimeField(auto_now=True)),
                ('function', models.CharField(max_length=256)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('start', models.IntegerField(default=0)),
                ('terms', models.IntegerField(default=0)),
                ('cd', models.IntegerField(default=0)),
                ('result', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=8191)),
                ('requested_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_arith_series_requester', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-requested_at'],
                'unique_together': {('function', 'start', 'terms', 'cd')},
            },
        ),
    ]
