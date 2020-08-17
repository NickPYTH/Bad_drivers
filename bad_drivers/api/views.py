from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import json
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView        
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Achivments, Reports
from rest_framework import serializers
from .serializers import AchivmentsSerializer, CreateReportsSerializer
from django.contrib.auth.models import User
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView)
from .permissions import IsOwnerProfileOrReadOnly

class AchivmentsListCreateView(ListCreateAPIView):
    queryset=Achivments.objects.all()
    serializer_class=AchivmentsSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = AchivmentsSerializer(queryset, many=True)
        return Response(serializer.data[0])

class CreateReport(ListCreateAPIView):
    serializer_class=CreateReportsSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

class GetUserReports(ListCreateAPIView):
    serializer_class=CreateReportsSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        None

    def get_queryset(self):
        status = json.loads(self.request.body.decode()).get("status")
        if status != "full":
            return Reports.objects.filter(user=self.request.user, report_status=status)
        else:
            return Reports.objects.filter(user=self.request.user)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CreateReportsSerializer(queryset, many=True)
        return Response(serializer.data)