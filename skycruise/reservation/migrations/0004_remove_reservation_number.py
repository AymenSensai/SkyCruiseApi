# Generated by Django 5.0.6 on 2024-05-27 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_reservation_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='number',
        ),
    ]