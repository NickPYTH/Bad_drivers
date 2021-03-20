from django.urls import path
from .views import CreateAchivmentView, CreateUserAchivmentView, GetAllAchivmentsList, GetUserAchivmentsList


urlpatterns = [
    path('create/', CreateAchivmentView.as_view(), name='create'),
    path('add_to_user/', CreateUserAchivmentView.as_view(), name='add_to_user'),
    path('all_achivments/', GetAllAchivmentsList.as_view(), name='all_achivments'),
    path('user_achivments/', GetUserAchivmentsList.as_view(), name='user_achivments'),
]