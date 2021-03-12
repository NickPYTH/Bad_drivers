from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ReportSerializer
from rest_framework import generics
from .models import Report

class ReportView(generics.CreateAPIView):
    queryset = Report.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ReportSerializer