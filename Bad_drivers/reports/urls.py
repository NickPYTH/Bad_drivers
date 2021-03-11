from django.urls import path
from .views import ReportView

urlpatterns = [
    path('send/', ReportView.as_view(), name='send_report'),
]