from django.contrib import admin
from django.urls import path
from mufc_club_app.views import home, learn_more, PlayerListAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('learn_more/', learn_more, name='learn-more'),
    path('api/players/', PlayerListAPI.as_view(), name='players-api'),
]
