# Generated by Django 2.2.5 on 2019-09-07 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_eventregister_email_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregister',
            name='email_id',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]