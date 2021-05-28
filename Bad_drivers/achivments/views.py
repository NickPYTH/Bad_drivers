from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .serializers import AchivmentSerializer, UserAchivmentSerializer
from rest_framework import generics
from .models import Achivment, UserAchivment
from rest_framework.response import Response

class CreateAchivmentView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AchivmentSerializer

class CreateUserAchivmentView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserAchivmentSerializer

class GetAllAchivmentsList(generics.ListCreateAPIView):
    queryset = Achivment.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AchivmentSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = AchivmentSerializer(queryset.all(), many=True)
        return Response(serializer.data)

class GetUserAchivmentsList(generics.ListCreateAPIView):
    queryset = UserAchivment.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserAchivmentSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserAchivmentSerializer(queryset.filter(user=request.user), many=True)
        return Response(serializer.data)