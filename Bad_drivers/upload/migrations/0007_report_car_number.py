# Generated by Django 3.1.3 on 2020-12-05 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_remove_report_car_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='car_number',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]