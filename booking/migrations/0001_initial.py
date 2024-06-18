# Generated by Django 4.2.13 on 2024-06-18 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_user', models.CharField(default=None, max_length=50, unique=True)),
                ('email_user', models.EmailField(blank=True, max_length=50)),
                ('phone_user', models.CharField(default=None, max_length=50)),
                ('number_of_guests', models.IntegerField(default=0, unique=True)),
                ('date_of_month', models.DateField(default=None)),
                ('time_of_day', models.TimeField(default=None)),
                ('message_to_restaurant', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cancel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='booking.reservation')),
            ],
        ),
    ]
