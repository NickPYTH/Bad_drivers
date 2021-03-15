from django.urls import path
from .views import SendReportView, UserReportList

urlpatterns = [
    path('send/', SendReportView.as_view(), name='send_report'),
    path('user-reports/', UserReportList.as_view(), name='user_reports_list'),
]