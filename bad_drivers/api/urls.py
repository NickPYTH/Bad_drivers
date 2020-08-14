from django.urls import path, re_path
from api import api_views
from rest_framework.authtoken import views

urlpatterns = [
    path('create-user', api_views.create_user),
    path('get-user-info', api_views.get_user_info),
    path('add-user-achivment', api_views.add_user_achivment),
    path('generate-session-token', api_views.generate_token),
    path('delete-session-token', api_views.delete_token),
]