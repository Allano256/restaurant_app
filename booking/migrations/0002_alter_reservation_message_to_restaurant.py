# Generated by Django 4.2.13 on 2024-07-12 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='message_to_restaurant',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
