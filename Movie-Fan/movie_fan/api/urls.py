from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views.sarp_views import MovieSarpView
from .views.auth_views import LoginView, LogoutView, RegisterView
from .views.model_views.game_view import GameView
from .views.model_views.category_view import CategoryView
from .views.model_views.player_view import PlayersView
from .views.model_views.join_game_view import JoinGameView
from .views.model_views.score_view import ScoreView
from .views.model_views.movie_view import MovieView
from .views.model_views.submition_view import SubmitionView


urlpatterns = [
    path('games/', GameView.as_view(), name='games'),
    path('games/<int:game_id>/', GameView.as_view(), name='game'),
    path('categories/<int:category_id>/', CategoryView.as_view()),
    path('players/', PlayersView.as_view(), name='players'),
    path('join/', JoinGameView.as_view(), name='join'),
    path('score/', ScoreView.as_view(), name='score'),
    path('category/', CategoryView.as_view(), name='categories'),
    path('category/<int:category_id>', CategoryView.as_view(), name='category'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('sarp_movie/', MovieSarpView.as_view(), name='sarp_movie'),
    path('movies/', MovieView.as_view(), name='movies'),
    path('submition/', SubmitionView.as_view(), name='submition'),
]
