from django.urls import path, re_path
from api import views

urlpatterns = [
    path('create-user', views.create_user),
    path('get-user-info', views.get_user_info),
    
]