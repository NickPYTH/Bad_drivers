from django.db import models
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User


class Achivment(models.Model):
    achivment_name = models.CharField(max_length=20, unique=True)
    achivment_description = models.TextField()
    big_image = models.CharField(max_length=200)
    small_image = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"

    def __str__(self):
        return str(self.achivment_name)

class UserAchivment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    achivment = models.ForeignKey(Achivment, on_delete=models.DO_NOTHING)
    date = models.DateField()

    class Meta:
        verbose_name = "Достижение пользователя"
        verbose_name_plural = "Достижения пользователей"

    def __str__(self):
        return '{0}  {1}'.format(str(self.user.username), str(self.achivment.achivment_name))


