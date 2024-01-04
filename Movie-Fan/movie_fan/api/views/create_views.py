from django.shortcuts import render
from rest_framework import generics, status
from ..serializers.create_serializers import *
from ..serializers.model_serializers import *
from ..models import Game, Movie, Player, Category, Submition
from rest_framework.views import APIView
from rest_framework.response import Response


class GameView(APIView):
    serializer_class = CreateGameSerializer

    def get(self, request, game_id=None, format=None):
        if game_id is not None:
            game = Game.objects.get(pk=game_id)
            categories = game.categories.all()
            category_data = CategorySerializer(categories, many=True).data

            serializer = GameSerializer(game)
            data = serializer.data
            data['categories'] = category_data

            return Response(data, status=status.HTTP_200_OK)
        
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        data = serializer.data

        for game_data in data:
            game = Game.objects.get(pk=game_data['id'])
            categories = game.categories.all()
            category_data = CategorySerializer(categories, many=True).data
            game_data['categories'] = category_data

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)


        if serializer.is_valid():
            name = serializer.data.get('name')
            description = serializer.data.get('description')
            categories = serializer.data.get('categories')
            host = self.request.session.session_key
            game = Game(name=name, description=description, 
            host=host)
            game.save()
            game.categories.set(categories)

            return Response(GameSerializer(game).data, status=status.HTTP_201_CREATED)
        
        return Response({'Bad Request': "1q12"}, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryView(APIView):
    serializer_class = CreateCategorySerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            description = serializer.data.get('description')
            category = Category(name=name, description=description)
            category.save()
            return Response(CategorySerializer(category).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': request}, status=status.HTTP_400_BAD_REQUEST)
    

