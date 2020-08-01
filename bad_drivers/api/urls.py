from django.urls import path, re_path
from .views import ApiView
from api import views
app_name = "api"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('api1/', ApiView.as_view()),
    path('create-user', views.create_user),
    
]