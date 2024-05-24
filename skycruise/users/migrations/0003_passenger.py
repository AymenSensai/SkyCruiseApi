# Generated by Django 5.0.6 on 2024-05-21 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_saved_flights'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('nationality', models.CharField(max_length=100, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('gender', models.BooleanField(null=True)),
                ('id_number', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
