# Generated by Django 3.1 on 2020-08-17 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20200817_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='user',
            field=models.IntegerField(default=0),
        ),
    ]
