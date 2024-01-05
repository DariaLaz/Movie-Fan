from django.shortcuts import render
from rest_framework import generics, status
from ..serializers.create_serializers import *
from ..serializers.model_serializers import *
from ..serializers.auth_serializers import *
from ..models import Game, Movie, Player, Category, Submition, PlayerScore
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout

class GameView(APIView):
    serialize_class = GameSerializer
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateGameSerializer
        elif self.request.method == 'PUT':
            return UpdateGameSerializer
        else:
            return GameSerializer

    def put(self, request):
        self.serializer_class = UpdateGameSerializer

        code = request.data.get('code')
        username = request.data.get('username')
            
        if code and username:
            player = Player.objects.get(name=username)
            game = Game.objects.get(code=code)
            if game.mode != 0:
                return Response({'Bad Request': "1q12"}, status=status.HTTP_400_BAD_REQUEST)
            
            game.participants.add(player)
            serializer = self.serializer_class(game, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                game.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
        
        return Response({'Bad Request': "gygh"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        self.serializer_class = GameSerializer
        game_id = request.GET.get('game_id')
        if game_id is not None:
            try:
                game = Game.objects.get(pk=game_id)
                categories = game.categories.all()
                category_data = CategorySerializer(categories, many=True).data

                serializer = GameSerializer(game)
                data = serializer.data
                data['categories'] = category_data

                return Response(data, status=status.HTTP_200_OK)
            except:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        
        
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
        self.serializer_class = self.get_serializer_class()
        
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)


        if serializer.is_valid():
            name = serializer.data.get('name')
            description = serializer.data.get('description')
            categories = serializer.data.get('categories')
            host = serializer.data.get('host')

            participant = Player.objects.get(name=host)

            game = Game(name=name, description=description, 
            host=host, mode=0)
            game.save()
            game.participants.add(participant)
            game.categories.set(categories)

            return Response(GameSerializer(game).data, status=status.HTTP_201_CREATED)
        
        return Response({'Bad Request': "1q12"}, status=status.HTTP_400_BAD_REQUEST)
    
class JoinGame(APIView):
    
    def post(self, request, code=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        if code is not None:
            res_game = Game.objects.filter(code=code)
            if len(res_game) != 0:
                game = res_game[0]
                

    
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
    

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "Successfully logged out"}, status=status.HTTP_200_OK)

    
class LoginView(APIView):
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            
            user = User.objects.get(username=serializer.data.get('username'))
            token, created = Token.objects.get_or_create(user=user)
            return Response({
            'token': token.key,
            'username': serializer.data.get('username'),
            'user_id': user.id
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    
class RegisterView(APIView):
    serializer_class = UserRegisterSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PlayersView(APIView):
    serializer_class = CreatePlayerSerializer

    def get(self, request, format=None):
        self.serializer_class = PlayerSerializer
        name = request.GET.get('name')
        player_id = request.GET.get('player_id')
        
        if player_id is not None:
            try:
                player = Player.objects.get(pk=player_id)
                serializer = PlayerSerializer(player)
                score = player.score
                score_data = ScoreSerializer(score).data
                data = serializer.data
                data['score'] = score_data

                my_games = player.my_games.all()
                my_games_data = GameSerializer(my_games, many=True).data

                data['my_games'] = my_games_data

                return Response(data, status=status.HTTP_200_OK)
            except:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        
        if name is not None:
            try:
                player = Player.objects.get(name=name)
                serializer = PlayerSerializer(player, many=False)
                score = player.score
                score_data = ScoreSerializer(score).data
                data = serializer.data
                data['score'] = score_data

                my_games = player.my_games.all()
                my_games_data = GameSerializer(my_games, many=True).data

                data['my_games'] = my_games_data
                return Response(data, status=status.HTTP_200_OK)
            except:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
            
        
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):

        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            user_id = User.objects.get(username=name)
            player = Player(name=name, user_id=user_id, score=PlayerScore.objects.create())
            player.save()

            return Response(PlayerSerializer(player).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ScoreView(APIView):
    serializer_class = ScoreSerializer
    def get(self, request, format=None):
        id = request.GET.get('id')
        try:
            score = PlayerScore.objects.get(id=id)
            return Response(ScoreSerializer(score).data, status=status.HTTP_200_OK)
        except:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)

