from django.urls import path
from .views import CreateAchivmentView, CreateUserAchivmentView


urlpatterns = [
    path('create/', CreateAchivmentView.as_view(), name='create'),
    path('add_to_user/', CreateUserAchivmentView.as_view(), name='add_to_user'),
]