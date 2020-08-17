from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserProfileListCreateView, UserProfileDetailView, UserProfileUpdate

urlpatterns = [
    path("create-full-profile", UserProfileListCreateView.as_view()),
    path("get-profile", UserProfileDetailView.as_view()),   
    path("update-profile", UserProfileUpdate.as_view()),
]