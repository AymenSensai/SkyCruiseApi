# Generated by Django 5.0.6 on 2024-05-26 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0010_alter_seat_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seat',
            old_name='number',
            new_name='seat_number',
        ),
    ]
