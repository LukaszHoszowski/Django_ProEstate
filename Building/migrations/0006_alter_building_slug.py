# Generated by Django 3.2.7 on 2021-09-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Building', '0005_building_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
