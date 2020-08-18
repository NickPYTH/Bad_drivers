from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .models import userProfile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
import json


class UserProfileListCreateView(ListCreateAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)
   
   def list(self, request):
	None

class UserProfileDetailView(ListCreateAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

    def get_queryset(self):
        data = userProfile.objects.get(user_name=self.request.user)
        return data

    def list(self, request):
        user_info = self.get_queryset()
        data = {
                    "user_name": user_info.user_name,
                    "user_real_name": user_info.user_real_name,
                    "user_email": user_info.user_email,
                    "recieved_reports": user_info.recieved_reports,
                    "send_reports": user_info.send_reports,
                    "decline_reports": user_info.decline_reports,
                    "processing_reports": user_info.processing_reports,
            }
        return Response(data)

class UserProfileUpdate(ListCreateAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]

    def perform_create(self, serializer):
        None

    def list(self, request):
        data = json.loads(request.body.decode())
        userProfile.objects.filter(user_name=self.request.user).update(
            user_name=data.get("user_name"),
            user_real_name=data.get("user_real_name"),
            user_email=data.get("user_email"),
            recieved_reports=data.get("recieved_reports"),
            send_reports=data.get("send_reports"),
            decline_reports=data.get("decline_reports"),
            processing_reports=data.get("processing_reports")
            )
        return Response()
