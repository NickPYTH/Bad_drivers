from django.urls import path
from .views import CreateAchivmentView


urlpatterns = [
    path('create/', CreateAchivmentView.as_view(), name='create_achivment'),
]