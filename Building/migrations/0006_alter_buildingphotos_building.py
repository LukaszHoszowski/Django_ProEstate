# Generated by Django 3.2.7 on 2021-09-24 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Building', '0005_auto_20210924_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingphotos',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Building.building'),
        ),
    ]
