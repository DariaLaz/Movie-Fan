from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...models import Game, Player
from ...serializers.model_serializers import GameSerializer
from ...serializers.create_serializers import JoinGameSerializer


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

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
