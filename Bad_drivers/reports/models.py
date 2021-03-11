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
        verbose_name = "Автомобили"
        verbose_name_plural = "Таблица автомобилей"

    def __str__(self):
        return str(str(self.car_number) + str(self.car_region))

class Report(models.Model):
    car_number = models.CharField(max_length=6)
    car_region = models.CharField(max_length=3)
    car_country = models.CharField(max_length=3)
    data = models.DateTimeField()
    status = models.BooleanField()
    description = models.TextField()

    image_1 = models.ImageField(upload_to="reports_images")
    image_2 = models.ImageField(upload_to="reports_images")
    image_3 = models.ImageField(upload_to="reports_images")

    class Meta:
        verbose_name = "Жалобы"
        verbose_name_plural = "Таблица жалоб"

    def __str__(self):
        return str(str("self.data.date") + str(self.status))

    
    