# Generated by Django 3.2.7 on 2021-09-24 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Building', '0004_auto_20210923_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='housingcooperative',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.CreateModel(
            name='BuildingPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='images/buildings/from_users/', verbose_name='Zdjęcie budynku')),
                ('picture_description', models.CharField(max_length=255, verbose_name='Opis zdjęcia')),
                ('building', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Building.building')),
            ],
            options={
                'verbose_name': 'Zdjęcie nieruchomości',
                'verbose_name_plural': 'Zdjęcia nieruchomości',
            },
        ),
        migrations.CreateModel(
            name='BuildingDocs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, upload_to='images/buildings/documents/', verbose_name='Zdjęcie budynku')),
                ('document_description', models.CharField(max_length=255, verbose_name='Opis dokumentu')),
                ('building', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Building.building')),
            ],
            options={
                'verbose_name': 'Dokument nieruchomości',
                'verbose_name_plural': 'Dokumenty nieruchomości',
            },
        ),
    ]