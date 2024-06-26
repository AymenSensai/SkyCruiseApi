# Generated by Django 5.0.6 on 2024-05-19 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=20)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    'arrival_airport',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='arrival_flights',
                        to='location.airport'
                    )
                ),
                (
                    'departure_airport',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='departure_flights',
                        to='location.airport'
                    )
                ),
            ],
        ),
    ]
