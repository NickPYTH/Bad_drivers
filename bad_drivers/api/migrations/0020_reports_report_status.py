# Generated by Django 3.1 on 2020-08-17 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20200817_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='report_status',
            field=models.CharField(default='processing', max_length=10),
        ),
    ]
