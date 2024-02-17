from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...models import Player, PlayerScore
from ...serializers.create_serializers import ScoreSerializer
from django.contrib.auth.models import User


class ScoreView(APIView):
    def get(self, request, format=None):
        """Returns all scores or for specific player if player_id is provided"""
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
