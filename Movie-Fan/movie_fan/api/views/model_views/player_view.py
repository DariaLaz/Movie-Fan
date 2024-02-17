from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...models import Player, PlayerScore
from ...serializers.model_serializers import PlayerSerializer, GameSerializer
from ...serializers.create_serializers import CreatePlayerSerializer, ScoreSerializer
from django.contrib.auth.models import User


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
            player = Player(name=name, user_id=user_id,
                            score=PlayerScore.objects.create())
            player.save()

            return Response(PlayerSerializer(player).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
