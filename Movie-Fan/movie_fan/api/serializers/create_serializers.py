from rest_framework import serializers
from ..models import Game, Player, Category, Submition, Movie


class CreateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game

        fields = ('name', 'description', 'categories', 'host')
        read_only_fields = ('code', 'created_at')

class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')
        read_only_fields = ('code', 'created_at')

class CreatePlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('name',)

class UpdateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('code',)