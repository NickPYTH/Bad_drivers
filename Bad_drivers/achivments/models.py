from django.db import models
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


class Achivments(models.Model):
    achivment_name = models.CharField(max_length=20)
    achivment_description = models.TextField()
    big_image = models.ImageField(upload_to="achivments_images")
    small_image = models.ImageField(upload_to="achivments_images")

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"

    def __str__(self):
        return str(self.achivment_name)
