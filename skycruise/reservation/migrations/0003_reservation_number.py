# Generated by Django 5.0.6 on 2024-05-27 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_remove_reservation_passengers_reservationseat'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='number',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
