from django.db import models
from django.contrib.auth.models import User
#from versatileimagefield.fields import VersatileImageField, PPOIField
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile

class Car(models.Model):
    car_number = models.CharField(max_length=6)
    car_region = models.CharField(max_length=3)
    car_country = models.CharField(max_length=3)

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return str(str(self.car_number) + str(self.car_region))

class Report(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Username', null=True, blank=True)
    car_number = models.CharField(max_length=6)
    car_region = models.CharField(max_length=3)
    car_country = models.CharField(max_length=3)
    data = models.DateTimeField()
    status = models.IntegerField(default=0)
    description = models.TextField()

    image_1 = models.ImageField(upload_to="reports_images")
    image_2 = models.ImageField(upload_to="reports_images")
    image_3 = models.ImageField(upload_to="reports_images")

    class Meta:
        verbose_name = "Жалоба"
        verbose_name_plural = "Жалобы"

    def __str__(self):
        return str(str("self.data.date") + str(self.status))
    
    