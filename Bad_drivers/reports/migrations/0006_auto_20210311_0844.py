# Generated by Django 3.1.7 on 2021-03-11 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20210310_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='car',
        ),
        migrations.AddField(
            model_name='report',
            name='car_country',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='car_number',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='car_region',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
    ]
