# Generated by Django 5.0.6 on 2024-05-24 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0008_seat'),
        ('reservation', '0001_initial'),
        ('users', '0006_remove_user_stripe_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='passengers',
        ),
        migrations.CreateModel(
            name='ReservationSeat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'passenger',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='reservation_seats',
                        to='users.passenger'
                    )
                ),
                (
                    'reservation',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='reservation_seats',
                        to='reservation.reservation'
                    )
                ),
                (
                    'seat',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='reservation_seats',
                        to='flight.seat'
                    )
                ),
            ],
        ),
    ]
