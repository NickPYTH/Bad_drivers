from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    real_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    send_report = models.IntegerField()
    decline_report = models.IntegerField()
    proccessing_report = models.IntegerField()

class Report(models.Model):
    user_name = models.CharField(max_length=20)
    description = models.TextField()
    car_number = models.CharField(max_length=10)
    image1 = models.FileField(upload_to=".")
    image1_link = models.CharField(max_length=20)
    image2 = models.FileField(upload_to=".")
    image2_link = models.CharField(max_length=20)
    image3 = models.FileField(upload_to=".")
    image3_link = models.CharField(max_length=20)
    status = models.IntegerField(default=2)

