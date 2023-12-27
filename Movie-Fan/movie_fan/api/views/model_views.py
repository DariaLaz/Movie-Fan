from django.shortcuts import render
from rest_framework import generics
from ..serializers.create_serializers import *
from ..serializers.model_serializers import *
from ..models import Game, Movie, Player, Category, Submition


class MovieView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class GamesView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class PlayersView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class CategoriesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubmitionsView(generics.ListAPIView):
    queryset = Submition.objects.all()
    serializer_class = SubmitionSerializer