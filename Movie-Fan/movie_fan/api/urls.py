from django.urls import path
from .views.create_views import *

urlpatterns = [
    path('games/', GameView.as_view()),
    path('games/<int:game_id>/', GameView.as_view()),
    # path('movie/', MovieView.as_view()),
    # path('player/', PlayersView.as_view()),
    # path('category/', CategoriesView.as_view()),
    # path('submition/', SubmitionsView.as_view()),
    path('category/', CategoryView.as_view()),

]