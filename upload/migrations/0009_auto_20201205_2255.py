# Generated by Django 3.1.3 on 2020-12-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0008_auto_20201205_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='image1_link',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='image2_link',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='image3_link',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
