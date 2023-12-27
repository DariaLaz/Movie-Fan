from django.shortcuts import render
from rest_framework import generics, status
from ..serializers.create_serializers import *
from ..serializers.model_serializers import *
from ..models import Game, Movie, Player, Category, Submition
from rest_framework.views import APIView
from rest_framework.response import Response


class CreateGameView(APIView):
    serializer_class = CreateGameSerializer

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
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
    
class CreateCategoryView(APIView):
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
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)