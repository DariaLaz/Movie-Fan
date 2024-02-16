from django.urls import path
from .views.module_views import *
from rest_framework.authtoken.views import obtain_auth_token
from .views.auth_views import *
from .views.sarp_views import MovieSarpView

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