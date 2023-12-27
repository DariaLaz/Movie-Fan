from django.urls import path
from .views.create_views import *
from .views.model_views import *
urlpatterns = [
    path('games', GamesView.as_view()),
    path('movie', MovieView.as_view()),
    path('player', PlayersView.as_view()),
    path('category', CategoriesView.as_view()),
    path('submition', SubmitionsView.as_view()),
    path('create-game', CreateGameView.as_view()),
    path('create-category', CreateCategoryView.as_view())
]