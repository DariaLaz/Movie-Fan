from rest_framework.views import APIView
from ..serializers.create_serializers import *
from ..serializers.model_serializers import *
from ..serializers.auth_serializers import *
from ..models import Game
from ..models import Player
from ..models import PlayerScore

from ..models import Category
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

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
        """Put request are used to start / finish game - change game mode"""
        self.serializer_class = GameSerializer

        game_id = request.data.get('game_id')
            
        if game_id is not None:
            try:
                game = Game.objects.get(pk=game_id)
                if game.mode == 0:
                    game.start()
                    game.unlock_next_categories()
                elif game.mode == 1:
                    game.finish()
                serializer = GameSerializer(game, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        return Response({'Bad Request': ""}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        """Get request are used to get all games or specific game if game_id is provided in request params the game is returned"""
        self.serializer_class = GameSerializer
        game_id = request.GET.get('game_id')
        username = request.GET.get('username')

        if game_id is not None:
            try:
                game = Game.objects.get(pk=game_id)
                player = Player.objects.get(name=username)

                categories = game.categories.all()
                category_data = CategorySerializer(categories, many=True).data

                for category in category_data:
                    #  0 - waiting for submitions, 1 - waiting for votes, 2 - finished, 3 - waiting for submition, 4 - waiting for vote, 5 - finished
                    print(category)
                    # if category['mode'] == 1 and category['submitions'].any(lambda id: id == player.id):
                    #    category['mode'] = 4
                    # elif category['mode'] == 2 and category['votes'].any(lambda id: id == player.id):
                    #     category['mode'] = 5                        

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

            for category in categories:
                cat = Category.objects.get(pk=category)    
                cat.game_id = game.id
                cat.save()

            game.categories.set(categories)
            participant.my_games.add(game)
            participant.score.all_games += 1
            participant.score.created += 1
            participant.score.save()
            participant.save()
            game.save()

            return Response(GameSerializer(game).data, status=status.HTTP_201_CREATED)
        
        return Response({'Bad Request': "1q12"}, status=status.HTTP_400_BAD_REQUEST)
    
class JoinGameView(APIView):
    
    def post(self, request, format=None):

        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = JoinGameSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.data.get('code')
            username = serializer.data.get('username')
            if code and username:
                player = None
                game = None
                try:
                    player = Player.objects.get(name=username)
                    game = Game.objects.get(code=code)
                except:
                    return Response({'Bad Request': "1q12"}, status=status.HTTP_400_BAD_REQUEST)
                
                if game.mode != 0:
                    return Response({'Bad Request': "1q12"}, status=status.HTTP_400_BAD_REQUEST)
                
                if game.participants.filter(name=username).exists():
                    return Response('Alreadyy in', status=status.HTTP_400_BAD_REQUEST)
                
                game.participants.add(player)
                player.my_games.add(game)
                player.update_score()
                # player.score.all_games += 1
                return Response(GameSerializer(game).data, status=status.HTTP_200_OK)


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
    
    def get(self, request, format=None):
        self.serializer_class = CategorySerializer
        category_id = request.GET.get('category_id')
        if category_id is not None:
            try:
                category = Category.objects.get(pk=category_id)
                serializer = CategorySerializer(category)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


    
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
        self.serializer_class = ScoreSerializer
        player_id = request.GET.get('player_id')
        if player_id is not None:
            try:
                player = Player.objects.get(pk=player_id)
                serializer = ScoreSerializer(player.score)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        
        scores = PlayerScore.objects.all()
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)