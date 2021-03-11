from rest_framework.permissions import AllowAny
from .serializers import ReportSerializer
from rest_framework import generics
from .models import Report

class ReportView(generics.CreateAPIView):
    queryset = Report.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ReportSerializer