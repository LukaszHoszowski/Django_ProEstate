# Generated by Django 3.2.7 on 2021-09-23 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Building', '0002_auto_20210923_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='building',
            old_name='slug_building',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='flat',
            old_name='slug_flat',
            new_name='slug',
        ),
    ]
