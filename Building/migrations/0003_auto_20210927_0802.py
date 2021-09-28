# Generated by Django 3.2.7 on 2021-09-27 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Building', '0002_remove_flat_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.SmallIntegerField(choices=[(1, 'Styczeń'), (2, 'Luty'), (3, 'Marzec'), (4, 'Kwiecień'), (5, 'Maj'), (6, 'Czerwiec'), (7, 'Lipiec'), (8, 'Sierpień'), (9, 'Wrzesień'), (10, 'Październik'), (11, 'Listopad'), (12, 'Grudzień')], verbose_name='Miesiąc rozliczeniowy')),
                ('year', models.SmallIntegerField(choices=[(1, 2021), (2, 2022)], verbose_name='Rok rozliczeniowy')),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gas', models.DecimalField(decimal_places=1, max_digits=6, verbose_name='Gaz')),
                ('energy', models.DecimalField(decimal_places=1, max_digits=6, verbose_name='Prąd')),
                ('water', models.DecimalField(decimal_places=1, max_digits=6, verbose_name='Woda')),
                ('payment_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Building.paymentperiod', verbose_name='Okres rozliczeniowy')),
            ],
        ),
        migrations.AddField(
            model_name='flat',
            name='measure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Building.measure', verbose_name='Wskazania liczników'),
        ),
    ]