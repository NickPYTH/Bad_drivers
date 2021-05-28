from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from django_file_validator.validators import MaxSizeValidator


class Achivment(models.Model):
    achivment_name = models.CharField(max_length=20, unique=True, verbose_name="Название достижения", default=None)
    achivment_description = models.TextField(verbose_name="Описание достижения", max_length=300, default=None)
    big_image = models.ImageField(upload_to="achivments_images", verbose_name="Большая иконка", default=None,
                                  validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']),
                                              MaxSizeValidator(2048)])

    small_image = models.ImageField(upload_to="achivments_images", verbose_name="Маленькая иконка", default=None,
                                    validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']),
                                                MaxSizeValidator(512)]
                                    )

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"

    def __str__(self):
        return str(self.achivment_name)

class UserAchivment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Пользователь")
    achivment = models.ForeignKey(Achivment, on_delete=models.DO_NOTHING, verbose_name="Достижение")
    date = models.DateField(verbose_name="Дата получения")

    class Meta:
        verbose_name = "Достижение пользователя"
        verbose_name_plural = "Достижения пользователей"

    def __str__(self):
        return '{0}  {1}'.format(str(self.user.username), str(self.achivment.achivment_name))


