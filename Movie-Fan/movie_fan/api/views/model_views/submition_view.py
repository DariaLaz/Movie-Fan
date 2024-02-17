from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...models import Submition, Category, Player, Movie, Game
from ...serializers.create_serializers import CreateSubmitionSerializer
from ...serializers.model_serializers import SubmitionSerializer, MovieSerializer, PlayerSerializer


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

                submition = Submition(
                    category=category, player=player, movie=movie)
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
                data = SubmitionSerializer(submitions, many=True).data
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
