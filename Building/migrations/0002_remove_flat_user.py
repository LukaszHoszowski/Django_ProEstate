# Generated by Django 3.2.7 on 2021-09-26 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Building', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='user',
        ),
    ]
