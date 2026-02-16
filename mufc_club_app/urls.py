from .views import home, learn_more, PlayerListAPI, players_list, fan_zone
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('learn_more/', learn_more, name='learn-more'),
    path('api/players/', PlayerListAPI.as_view(), name='players-api'),
    path('squad/', players_list, name='players_list'),
    path('fans/',  fan_zone, name='fan_zone'),
]
