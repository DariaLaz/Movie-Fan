from ...models import Game
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ...serializers.create_serializers import CreateGameSerializer
from ...serializers.model_serializers import GameSerializer, CategorySerializer
from ...models import Category, Player


class GameView(APIView):
    def put(self, request):
        """Put request are used to start game - change game mode"""
        try:
            game_id = request.data.get('game_id')
            # game_id = request.GET.get('game_id')

            if game_id is not None:
                game = Game.objects.get(pk=game_id)
                if game.mode == 0:
                    if game.num_of_players() < 3:
                        return Response({"Wrong": "Min 3 players"}, status=status.HTTP_400_BAD_REQUEST)
                    game.start()
                    game.unlock_next_categories()
                serializer = GameSerializer(
                    game, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'Bad Request': ""}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)

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
        sortedRes = sorted(result.items(), key=lambda x: x[1], reverse=True)
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
        try:
            game_id = request.data.get('game_id')

            if game_id is not None:
                game = Game.objects.get(pk=game_id)

                if game.mode != 0:
                    return Response('Cannot delete game once it has started', status=status.HTTP_400_BAD_REQUEST)

                for category in game.categories.all():
                    Category.objects.get(pk=category.id).delete()

                game.delete()
                return Response("Deleted", status=status.HTTP_200_OK)
            else:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        except:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)
