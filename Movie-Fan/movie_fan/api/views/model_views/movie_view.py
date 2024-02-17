from ...models import Movie
from ...serializers.create_serializers import CreateMovieSerializer
from ...serializers.model_serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
            movie = Movie(title=title, description=description,
                          genre=genre, tumbnail=tumbnail, link=link, rating=rating)
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
