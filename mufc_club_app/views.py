from django.shortcuts import render
from .models import Player
from .serializers import PlayerSerializer
from rest_framework import generics


def home(request):
    return render(request, 'index.html')


def learn_more(request):
    return render(request, 'learn-more.html')


class PlayerListAPI(generics.ListAPIView):
    queryset = Player.objects.all().order_by('number')
    serializer_class = PlayerSerializer
