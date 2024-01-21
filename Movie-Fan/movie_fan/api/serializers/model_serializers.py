from rest_framework import serializers
from ..models import Game, Player, Category, Submition, Movie

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'code', 'host','created_at', 'name', 'description', 'participants', 'categories', 'mode')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'score', 'my_games')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'submitions', 'mode', 'game_id')

class SubmitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submition
        fields = ('id', 'player', 'movie')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'year', 'genre', 'tumbnail')

# class UserRegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Player
#         fields = ('id', 'name', 'password')