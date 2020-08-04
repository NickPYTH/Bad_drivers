from django.db import models

class Users(models.Model):
  user_name = models.CharField(max_length = 30, unique=True, default=None)
  user_real_name = models.CharField(max_length= 30, default=None)
  user_email = models.EmailField(unique=True, default=None)
  user_password = models.CharField(max_length = 30, unique=True, default=None)
  achivments_id = models.IntegerField(default=None)
  recieved_reports = models.IntegerField(default=None)
  send_reports = models.IntegerField(default=None)
  decline_reports = models.IntegerField(default=None)
  processing_reports = models.IntegerField(default=None)

class Achivments(models.Model):
  achivment_name = models.CharField(max_length= 30)
  achivment_description = models.TextField()
  achivment_icon_id = models.CharField(max_length= 10)

