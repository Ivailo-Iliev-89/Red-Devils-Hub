from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('mufc_club_app.urls', 'club'), namespace='club')),
]
