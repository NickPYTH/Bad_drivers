from django.urls import path
from .views import SendReportView, UserReportList, UserInfoList

urlpatterns = [
    path('send/', SendReportView.as_view(), name='send_report'),
    path('user-reports/', UserReportList.as_view(), name='user_reports_list'),
    path('user-info/', UserInfoList.as_view(), name='user_info'),
]