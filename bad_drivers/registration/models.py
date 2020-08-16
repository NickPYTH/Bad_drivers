from django.contrib.auth.models import User
from django.db import models


class userProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    user_name = models.CharField(max_length=20, default=None)
    user_real_name = models.CharField(max_length=20, default=None)
    user_email = models.EmailField(default=None)
    recieved_reports = models.IntegerField(default=0)
    send_reports = models.IntegerField(default=0)
    decline_reports = models.IntegerField(default=0)
    processing_reports = models.IntegerField(default=0)

    #description=models.TextField(blank=True,null=True)
    #location=models.CharField(max_length=30,blank=True)
    #date_joined=models.DateTimeField(auto_now_add=True)
    #updated_on=models.DateTimeField(auto_now=True)
    #is_organizer=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username