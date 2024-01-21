from django.urls import path
from .views.module_views import *
from rest_framework.authtoken.views import obtain_auth_token
from .views.auth_views import *
from .views.sarp_views import MovieView

urlpatterns = [
    path('games/', GameView.as_view()),
    path('games/<int:game_id>/', GameView.as_view()),
    path('categories/<int:category_id>/', CategoryView.as_view()),
    path('players/', PlayersView.as_view()),
    path('join/', JoinGameView.as_view()),
    path('score/', ScoreView.as_view()),
    path('category/', CategoryView.as_view()),
    path('login/', LoginView.as_view(), name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('movie/', MovieView.as_view()),
]