# Generated by Django 4.2.13 on 2024-06-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, unique=True)),
                ('last_name', models.CharField(max_length=200, unique=True)),
                ('customer_email', models.CharField(max_length=200, unique=True)),
                ('number_of_tables', models.IntegerField(default=0)),
                ('number_of_guests', models.IntegerField(default=0)),
                ('message_to_restaurant', models.TextField()),
                ('booked_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
