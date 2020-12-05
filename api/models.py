from django.db import models
from registration import models as reg_models
from hakaton import settings


class Achivment(models.Model):
  #achivment_user = models.ForeignKey(Users, on_delete=models.CASCADE, default=0)
    achivment_name = models.CharField(max_length= 30)
    achivment_description = models.TextField()
    achivment_icon_id = models.CharField(max_length= 10)


class Report(models.Model):
    user = models.CharField(max_length=15, default=None)
    report_description = models.CharField(max_length=50)
    report_picture = models.ImageField(upload_to="", height_field=None, width_field=None, max_length=100)
  
    report_status = models.CharField(max_length=10, default="processing")

     


  

