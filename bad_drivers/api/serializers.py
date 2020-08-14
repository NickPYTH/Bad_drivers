from rest_framework import serializers
from .models import Achivments

class UserSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    user_real_name = serializers.CharField()
    user_email = serializers.EmailField()
    user_password = serializers.CharField()
    reports_id = serializers.IntegerField()
    achivments_id = serializers.IntegerField()
    recieved_reports = serializers.IntegerField()
    send_reports = serializers.IntegerField()
    decline_reports = serializers.IntegerField()
    processing_reports = serializers.IntegerField()

class AchivmentsSerializer(serializers.Serializer):
    id = serializers.ImageField(read_only=True)
    achivment_name = serializers.CharField()
    achivment_description = serializers.CharField(style={'base_template': 'textarea.html'})
    achivment_icon_id = serializers.CharField()


