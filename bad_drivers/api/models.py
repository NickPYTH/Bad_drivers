from django.db import models
from registration import models as reg_models
from bad_drivers import settings

class Achivments(models.Model):
  #achivment_user = models.ForeignKey(Users, on_delete=models.CASCADE, default=0)
  achivment_name = models.CharField(max_length= 30)
  achivment_description = models.TextField()
  achivment_icon_id = models.CharField(max_length= 10)



class Reports(models.Model):
  user = models.CharField(max_length=15, default=None)
  report_description = models.CharField(max_length=50)
  report_picture = models.ImageField(upload_to=settings.STATIC_URL, height_field=None, width_field=None, max_length=100)
  
  report_status = models.CharField(max_length=10, default="processing")

     


  

