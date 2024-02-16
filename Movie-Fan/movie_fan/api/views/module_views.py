from rest_framework.views import APIView
from ..serializers.create_serializers import *
from ..serializers.model_serializers import *
from ..serializers.auth_serializers import *
from ..models import Game
from ..models import Player
from ..models import PlayerScore
from ..models import Submition

from ..models import Category
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class GameView(APIView):
    def put(self, request):
        """Put request are used to start game - change game mode"""
        game_id = request.data.get('game_id')
            
        if game_id is not None:
            try:
                game = Game.objects.get(pk=game_id)
                if game.mode == 0:
                    if game.num_of_players() < 3:
                        return Response({"Wrong":"Min 3 players"}, status=status.HTTP_400_BAD_REQUEST)
                    game.start()
                    game.unlock_next_categories()
                serializer = GameSerializer(game, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        return Response({'Bad Request': ""}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        """Get request returns all games or specific game if game_id is provided in request params"""
        game_id = request.GET.get('game_id')

        if game_id is not None: 
            """If game_id is provided, return specific game with all categories and submitions for each category"""
            try:
                game = Game.objects.get(pk=game_id)

                categories = game.categories.all()
                category_data = CategorySerializer(categories, many=True).data

                #  0 - waiting for submitions, 1 - waiting for votes, 2 - finished, 3 - waiting for submition, 4 - waiting for vote, 5 - finished                      

                serializer = GameSerializer(game)
                data = serializer.data
                data['categories'] = category_data

                if game.mode == 2:
                    data['results'] = self.__get_result(categories=categories)

                return Response(data, status=status.HTTP_200_OK)
            except:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        
        """If game_id is not provided, return all games with all categories"""
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        data = serializer.data

        for game_data in data:
            game = Game.objects.get(pk=game_data['id'])
            categories = game.categories.all()
            category_data = CategorySerializer(categories, many=True).data
            game_data['categories'] = category_data

        return Response(data, status=status.HTTP_200_OK)
    
    def __get_result(self, categories):
        """Get result of the game based on categories and submitions for each category"""
        result = {}
        for category in categories:
            for submition in category.submitions.all():
                if submition.player.name not in result:
                    result[submition.player.name] = 0
                result[submition.player.name] += submition.points
        sortedRes  = sorted(result.items(), key=lambda x:x[1], reverse=True)
        return dict(sortedRes)

    def post(self, request, format=None):  
        """Post request are used to create new game"""     

        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = CreateGameSerializer(data=request.data)

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
        
        return Response({'Bad Request': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        """Delete request are used to delete game"""
        game_id = request.data.get('game_id')
        
        if game_id is not None:
            try:
                game = Game.objects.get(pk=game_id)

                if game.mode != 0:
                    return Response('Cannot delete game once it has started', status=status.HTTP_400_BAD_REQUEST)

                for category in game.categories.all():
                    Category.objects.get(pk=category.id).delete()

                game.delete()
                return Response("Deleted", status=status.HTTP_200_OK)
            except:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        return Response("Not found", status=status.HTTP_404_NOT_FOUND)  
    
class JoinGameView(APIView):
    def post(self, request, format=None):
        """Post request are used to join game"""
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
                    return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)
                
                if game.mode != 0:
                    return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)
                
                if game.participants.filter(name=username).exists():
                    return Response('Already in', status=status.HTTP_400_BAD_REQUEST)
                
                game.participants.add(player)
                player.my_games.add(game)
                player.update_score()
                return Response(GameSerializer(game).data, status=status.HTTP_200_OK)
            
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
class CategoryView(APIView):
    serializer_class = CreateCategorySerializer

    def put(self, request, format=None):
        """Put request are used to vote for submitions in category"""
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        try:
            category_id = request.GET.get('category_id')
            username = request.GET.get('username')
            player = Player.objects.get(name=username)
            category = Category.objects.get(pk=category_id)
            game = Game.objects.get(pk=category.game_id)

            if category.has_voted(player):
                return Response('Already voted', status=status.HTTP_400_BAD_REQUEST)

            for key in request.data.keys():
                submition_id = key
                points = request.data[key]
                
                submition = Submition.objects.get(pk=submition_id)
                submition.add_points(points)

                game.update_results(player=submition.player, points=points)

            category.add_voter(player)


            if category.num_of_votes() == category.num_of_submitions():
                category.finish()
                
                if not game.unlock_next_categories():
                    game.finish()

            return Response(GameSerializer(game), status=status.HTTP_200_OK)
        except:
            return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        """Post request are used to create new category"""
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = CreateCategorySerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data.get('name')
            description = serializer.data.get('description')
            category = Category(name=name, description=description)
            category.save()
            return Response(CategorySerializer(category).data, status=status.HTTP_201_CREATED)
        
        return Response({'Bad Request': request}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        """Get request returns all categories or specific category if category_id is provided in request params"""
        
        self.serializer_class = CategorySerializer
        category_id = request.GET.get('category_id')
        if category_id is not None:
            """If category_id is provided, return specific category with all submitions and voters for that category"""
            try:
                category = Category.objects.get(pk=category_id)
                serializer = CategorySerializer(category)
                data = serializer.data
                submitions = category.submitions.all()
                submitions_data = SubmitionSerializer(submitions, many=True).data
                data['submitions'] = submitions_data
                for submition in submitions_data:
                    movie = Movie.objects.get(pk=submition['movie'])
                    player = Player.objects.get(pk=submition['player'])
                    submition['movie'] = MovieSerializer(movie).data
                    submition['player'] = PlayerSerializer(player).data

                voters = category.voters.all()
                voters_data = PlayerSerializer(voters, many=True).data
                data['voters'] = voters_data
                for voter in voters_data:
                    name = voter['name']
                    voter['name'] = name


                return Response(data, status=status.HTTP_200_OK)
            except:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        
        """If category_id is not provided, return all categories"""
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, format=None):
        """Delete request are used to delete category"""
        category_id = request.GET.get('category_id')
        if category_id is not None:
            try:
                category = Category.objects.get(pk=category_id)
                category.delete()
                return Response("Deleted", status=status.HTTP_200_OK)
            except:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        return Response("Not found", status=status.HTTP_404_NOT_FOUND)
    

class SubmitionView(APIView):    
    def post(self, request, format=None):
        """Post request are used to create new submition"""
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = CreateSubmitionSerializer(data=request.data)

        if serializer.is_valid():
            category_id = serializer.data.get('category_id')
            username = serializer.data.get('username')
            movie_id = serializer.data.get('movie_id')
            
            try:
                category = Category.objects.get(pk=category_id)
                player = Player.objects.get(name=username)
                movie = Movie.objects.get(id=movie_id)

                game = Game.objects.get(pk=category.game_id)
                
                if not game or not game.participants.contains(player):
                    return Response({'Bad Request'"You are not part of that game"}, status=status.HTTP_400_BAD_REQUEST)

                if category.has_submition(player):
                    return Response({'Bad Request': "You already submited for that category"}, status=status.HTTP_400_BAD_REQUEST)

                submition = Submition(category=category, player=player, movie=movie)
                submition.save()

                category.add_submition(submition=submition)
                category.save()

                if category.num_of_submitions() == game.num_of_players():
                    category.start_voting()
                    category.save()

                return Response(SubmitionSerializer(submition).data, status=status.HTTP_201_CREATED)
            except:
                return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)
            
        return Response({'Bad Request': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
           
    def get(self, request, format=None):
        """Get request returns all submitions or specific ones if category_id or submition_id is provided in request params"""
        self.serializer_class = SubmitionSerializer
        submition_id = request.GET.get('submition_id')
        category_id = request.GET.get('category_id')
        if category_id is not None:
            """Returns the submitions for provided category"""
            try:
                submitions = Submition.objects.all().filter(category=category_id)
                data =  SubmitionSerializer(submitions, many=True).data
                for submition in data:
                    movie = Movie.objects.get(pk=submition['movie'])
                    player = Player.objects.get(pk=submition['player'])
                    submition['movie'] = MovieSerializer(movie).data
                    submition['player'] = PlayerSerializer(player).data
                return Response(data, status=status.HTTP_200_OK)
            except:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        if submition_id is not None:
            """Returns submition with provided submition_id"""
            try:
                submition = Submition.objects.get(pk=submition_id)
                serializer = SubmitionSerializer(submition)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        
        """Returns all submitions"""
        submitions = Submition.objects.all()
        serializer = SubmitionSerializer(submitions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class PlayersView(APIView):
    def get(self, request, format=None):
        """Get request returns all players or specific player if player_id or name is provided in request params"""
        name = request.GET.get('name')
        player_id = request.GET.get('player_id')
        
        if player_id is not None:
            """Returns a specific player if player_id is provided"""
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
            """Returns a specific player if name is provided"""
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
        """Post request are used to create new player"""
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = CreatePlayerSerializer(data=request.data)

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
        """Returns all scores or for specific player if player_id is provided"""
        self.serializer_class = ScoreSerializer
        player_id = request.GET.get('player_id')
        if player_id is not None:
            """Returns score for a specific player"""
            try:
                player = Player.objects.get(pk=player_id)
                serializer = ScoreSerializer(player.score)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        
        """Returns all scores"""
        scores = PlayerScore.objects.all()
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MovieView(APIView):
    def post(self, request, format=None):
        """Post request are used to create new movie"""
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = CreateMovieSerializer(data=request.data)

        if serializer.is_valid():
            title = serializer.data.get('title')
            description = serializer.data.get('description')
            genre = serializer.data.get('genre')
            tumbnail = serializer.data.get('tumbnail')
            link = serializer.data.get('link')
            rating = serializer.data.get('rating')
            movie = Movie(title=title, description=description, genre=genre, tumbnail=tumbnail, link=link, rating=rating)
            movie.save()
            return Response(MovieSerializer(movie).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        """Returns all movies or a specific movie if movie_id is provided"""
        movie_id = request.GET.get('movie_id')
        if movie_id is not None:
            """Returns a specific movie"""
            try:
                movie = Movie.objects.get(pk=movie_id)
                serializer = MovieSerializer(movie)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        
        """Returns all movies"""
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)