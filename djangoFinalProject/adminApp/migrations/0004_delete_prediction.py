# Generated by Django 5.1.3 on 2024-11-29 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0003_rename_ph_prediction_soilph'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Prediction',
        ),
    ]