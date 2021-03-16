from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .serializers import ReportSerializer, UserSerializer
from rest_framework import generics
from .models import Report
from rest_framework.response import Response

class SendReportView(generics.CreateAPIView):
    queryset = Report.objects.all()
    #authentication_classes = [AllowAny, ] # SessionAuthentication
    permission_classes = (IsAuthenticated,)
    #permission_classes = (AllowAny,)
    serializer_class = ReportSerializer

class UserReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    #serializer_class = UserSerializer
    #permission_classes = [IsAdminUser]
    permission_classes = (IsAuthenticated,)
    serializer_class = ReportSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ReportSerializer(queryset.filter(user_name=request.user), many=True)
        return Response(serializer.data)

class UserInfoList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset.filter(username=request.user), many=True)
        return Response(serializer.data)


