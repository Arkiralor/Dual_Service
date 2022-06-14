# Generated by Django 4.0.4 on 2022-04-23 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExtAPIs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arithseriesmodel',
            options={'ordering': ['-requested_at'], 'verbose_name': 'Arithmetic Series', 'verbose_name_plural': 'Arithmetic Series'},
        ),
        migrations.AlterModelOptions(
            name='binarytointmodel',
            options={'ordering': ['-requested_at'], 'verbose_name': 'Binary to Int', 'verbose_name_plural': 'Binary to Integers'},
        ),
        migrations.AlterModelOptions(
            name='factor',
            options={'ordering': ['-requested_at'], 'verbose_name': 'Factor', 'verbose_name_plural': 'Factors'},
        ),
        migrations.AlterModelOptions(
            name='fibonaccimodel',
            options={'ordering': ['-requested_at'], 'verbose_name': 'Fibonacci Sequence', 'verbose_name_plural': 'Fibonacci Sequences'},
        ),
        migrations.AlterModelOptions(
            name='geoseriesmodel',
            options={'ordering': ['-requested_at'], 'verbose_name': 'Geometric Series', 'verbose_name_plural': 'Geometric Series'},
        ),
        migrations.AlterModelOptions(
            name='inttobinarymodel',
            options={'ordering': ['-requested_at'], 'verbose_name': 'Int to Binary', 'verbose_name_plural': 'Int to Binaries'},
        ),
        migrations.AlterModelOptions(
            name='prime',
            options={'ordering': ['-requested_at'], 'verbose_name': 'Prime Number', 'verbose_name_plural': 'Prime Numbers'},
        ),
        migrations.AlterModelOptions(
            name='primefactormodel',
            options={'ordering': ['-requested_at'], 'verbose_name': 'Prime Factor', 'verbose_name_plural': 'Prime Factors'},
        ),
        migrations.AlterModelOptions(
            name='projectilepath2dmodel',
            options={'ordering': ['-requested_at'], 'verbose_name': '2D Projectile Path', 'verbose_name_plural': '2D Projectile Paths'},
        ),
    ]