from django.contrib import admin
from .models import Achivments

@admin.register(Achivments)
class AchivmentsAdmin(admin.ModelAdmin):
    list_display = ("achivment_name", "achivment_description")