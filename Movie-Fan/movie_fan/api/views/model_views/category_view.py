from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...models import Category, Player, Submition, Game, Movie
from ...serializers.create_serializers import CreateCategorySerializer
from ...serializers.model_serializers import CategorySerializer, SubmitionSerializer, PlayerSerializer, GameSerializer, MovieSerializer


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

            return Response(GameSerializer(game).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response('Bad Request', e)

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

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
                submitions_data = SubmitionSerializer(
                    submitions, many=True).data
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
        try:
            category_id = request.data.get('category_id')
            if category_id is not None:
                category = Category.objects.get(pk=category_id)
                category.delete()
                return Response("Deleted", status=status.HTTP_200_OK)
            else:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        except:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)
