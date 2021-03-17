from django.contrib import admin
from .models import Achivment, UserAchivment

@admin.register(Achivment)
class AchivmentAdmin(admin.ModelAdmin):
    list_display = ("achivment_name", "achivment_description")

@admin.register(UserAchivment)
class UserAchivmentAdmin(admin.ModelAdmin):
    list_display = ("user", "achivment")
    list_filter = ("user", "achivment", "date")