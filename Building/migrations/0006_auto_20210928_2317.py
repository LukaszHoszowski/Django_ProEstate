# Generated by Django 3.2.7 on 2021-09-28 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Building', '0005_auto_20210927_0834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flat',
            options={'ordering': ['building', 'number'], 'verbose_name': 'Mieszkanie', 'verbose_name_plural': 'Mieszkania'},
        ),
        migrations.AlterModelOptions(
            name='paymentperiod',
            options={'ordering': ('year', '-month'), 'verbose_name': 'Okres rozliczeniowy', 'verbose_name_plural': 'Okresy rozliczeniowe'},
        ),
        migrations.RemoveField(
            model_name='housingcooperative',
            name='president',
        ),
        migrations.AlterField(
            model_name='building',
            name='picture',
            field=models.ImageField(upload_to='images/buildings/', verbose_name='Zdjęcie budynku'),
        ),
        migrations.AlterField(
            model_name='paymentperiod',
            name='year',
            field=models.SmallIntegerField(choices=[(1, '2021'), (2, '2022')], verbose_name='Rok rozliczeniowy'),
        ),
    ]