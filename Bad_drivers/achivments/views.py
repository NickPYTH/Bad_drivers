from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .serializers import AchivmentSerializer, UserAchivmentSerializer
from rest_framework import generics
from .models import Achivment
from rest_framework.response import Response

class CreateAchivmentView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AchivmentSerializer

class CreateUserAchivmentView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserAchivmentSerializer