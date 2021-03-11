from django.contrib import admin
from .models import Car, Report

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("car_number", "car_region")
    list_filter = ("car_number", "car_region")

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("car_number", "car_region")
    list_filter = ("car_number", "car_region")

