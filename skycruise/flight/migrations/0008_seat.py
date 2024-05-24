# Generated by Django 5.0.6 on 2024-05-24 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0007_flightstepover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_class', models.CharField(max_length=20)),
                ('number', models.PositiveIntegerField()),
                (
                    'flight',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='flight.flight'
                    )
                ),
            ],
        ),
    ]