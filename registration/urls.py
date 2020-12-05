from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserProfileListCreateView, UserProfileDetailView, UserProfileUpdate

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path("create-full-profile", UserProfileListCreateView.as_view()),
    path("get-profile", UserProfileDetailView.as_view()),   
    path("update-profile", UserProfileUpdate.as_view()),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
