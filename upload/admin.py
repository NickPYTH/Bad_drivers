from django.contrib import admin
from .models import User, Report


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email")

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("user_name", "description")
