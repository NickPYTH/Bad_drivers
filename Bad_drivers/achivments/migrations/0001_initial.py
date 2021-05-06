# Generated by Django 3.1.7 on 2021-03-17 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achivments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achivment_name', models.CharField(max_length=20)),
                ('achivment_description', models.TextField()),
                ('big_image', models.ImageField(upload_to='achivments_images')),
                ('small_image', models.ImageField(upload_to='achivments_images')),
            ],
            options={
                'verbose_name': 'Достижение',
                'verbose_name_plural': 'Достижения',
            },
        ),
    ]