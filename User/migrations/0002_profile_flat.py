# Generated by Django 3.2.7 on 2021-09-26 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Building', '0002_remove_flat_user'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='flat',
            field=models.ManyToManyField(blank=True, to='Building.Flat'),
        ),
    ]
