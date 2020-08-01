from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .models import User

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
    processing_reports = serializers.IntegerField( )

class ApiView(APIView):
    def get(self, request):
        user = User()
        serializer = UserSerializer(user)
        data = User.objects.all()
        return Response({"user_info": serializer.data})
    

@csrf_exempt    
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        User.objects.create(
            user_name=data.get("user_name"),
            user_real_name=data.get("user_real_name"),    
            user_email=data.get("user_email"),
            user_password=data.get("user_password"),
            reports_id=data.get("reports_id"),
            achivments_id=data.get("achivments_id"),
            recieved_reports=data.get("recieved_reports"),
            send_reports=data.get("send_reports"),
            decline_reports=data.get("decline_reports"),
            processing_reports=data.get("processing_reports"),                     
            )
        return HttpResponse("post") 
    elif request.method == 'GET':
        return HttpResponse("get")

