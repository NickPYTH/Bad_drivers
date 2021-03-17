from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .serializers import AchivmentSerializer
from rest_framework import generics
from .models import Achivments
from rest_framework.response import Response

class CreateAchivmentView(generics.CreateAPIView):
    queryset = Achivments.objects.all()
    #authentication_classes = [AllowAny, ] # SessionAuthentication
    permission_classes = (IsAuthenticated,)
    #permission_classes = (AllowAny,)
    serializer_class = AchivmentSerializer