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
