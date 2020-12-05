from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from upload.views import registration, login, push_report, pull_report

urlpatterns = [
    path("registration/", registration, name="reg"),
    path("login/", login, name="login"),
    path("push_report/", push_report, name="push_report"),
    path("pull_report/", pull_report, name="pull_report"),
    path("admin/", admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
