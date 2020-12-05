# Register your models here.
from django.contrib import admin
from .models import userProfile
# Register your models here.

@admin.register(userProfile)
class userProfileAdmin(admin.ModelAdmin):
    list_display = ("user_name", "recieved_reports", "send_reports", "decline_reports", "processing_reports")
