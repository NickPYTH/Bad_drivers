# Generated by Django 3.1.3 on 2020-12-05 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_auto_20201205_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='car_number',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.FileField(upload_to='.'),
        ),
    ]
