from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView        
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Users, Achivments, ActualTokens
from rest_framework import serializers
from .serializers import UserSerializer, AchivmentsSerializer
from django.contrib.auth.models import User
from uuid import uuid4

def token_check(token):
    if list(ActualTokens.objects.filter(token=token)):
        return True
    else:
        return False

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        if token_check(data.get("token")):
            Users.objects.create(
                user_name=data.get("user_name"),
                user_real_name=data.get("user_real_name"),    
                user_email=data.get("user_email"),
                user_password=data.get("user_password"),
                achivments_id=data.get("achivments_id"),
                recieved_reports=data.get("recieved_reports"),
                send_reports=data.get("send_reports"),
                decline_reports=data.get("decline_reports"),
                processing_reports=data.get("processing_reports"),                     
                )
            return HttpResponse()
    return HttpResponse()

@csrf_exempt
def get_user_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        if token_check(data.get("token")):
            try:
                user_info = Users.objects.get(user_name=data.get("user_name"))
                data = {
                    "user_name": user_info.user_name,
                    "user_real_name": user_info.user_real_name,
                    "user_email": user_info.user_email,
                    "user_password": user_info.user_password,
                    "achivments_id": user_info.achivments_id,
                    "recieved_reports": user_info.recieved_reports,
                    "send_reports": user_info.send_reports,
                    "decline_reports": user_info.decline_reports,
                    "processing_reports": user_info.processing_reports,
                }
                return HttpResponse(json.dumps(data))
            except:
                return HttpResponse(json.dumps({"Error": "Name not found"}))
        return HttpResponse()

@csrf_exempt
def add_user_achivment(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        if token_check(data.get("token")):
            Achivments.objects.create(
                    achivment_name=data.get("achivment_name"),
                    achivment_description=data.get("achivment_description"),
                    achivment_icon_id=data.get("achivment_icon_id"),                   
                )
            return HttpResponse(data.get("token"))
    return HttpResponse()

def generate_token(request):
    if request.method == 'GET':
        token = uuid4()
        ActualTokens.objects.create(
            token=token,                   
            )
        return HttpResponse(token)
    return HttpResponse()

@csrf_exempt
def delete_token(request):
    if request.method == "POST":
        data = json.loads(request.body.decode())
        ActualTokens.objects.get(token=data.get("token")).delete()
    return HttpResponse()



