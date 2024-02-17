from rest_framework import serializers
from ..models import Game, Player, Category, Movie
from ..models import PlayerScore


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


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerScore
        fields = '__all__'


class JoinGameSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)
    username = serializers.CharField(max_length=50)


class CreateSubmitionSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    category_id = serializers.IntegerField()
    movie_id = serializers.IntegerField()


class CreateMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'rating',
                  'genre', 'tumbnail', 'link')
