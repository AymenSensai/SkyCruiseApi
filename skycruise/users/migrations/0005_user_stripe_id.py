# Generated by Django 5.0.6 on 2024-05-23 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_passenger_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
