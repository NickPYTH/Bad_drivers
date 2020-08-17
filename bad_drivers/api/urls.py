from django.urls import path, re_path
from api import views
from .views import CreateReport, GetUserReports

urlpatterns = [
    path("create-report", CreateReport.as_view()),
    path("get-user-reports-by-status", GetUserReports.as_view()),
]