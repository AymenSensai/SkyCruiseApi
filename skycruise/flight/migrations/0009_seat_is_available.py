# Generated by Django 5.0.6 on 2024-05-24 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0008_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]