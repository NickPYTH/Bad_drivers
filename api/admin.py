# Register your models here.
from django.contrib import admin
from .models import Achivment, Report
# Register your models here.

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("user",)


@admin.register(Achivment)
class AchivmentAdmin(admin.ModelAdmin):
    list_display = ("achivment_name", "achivment_description")


