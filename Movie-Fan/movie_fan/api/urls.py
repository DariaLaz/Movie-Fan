from django.urls import path
from .views.create_views import *
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('games/', GameView.as_view()),
    path('games/<int:game_id>/', GameView.as_view()),
    path('players/', PlayersView.as_view()),
    # path('movie/', MovieView.as_view()),
    # path('player/', PlayersView.as_view()),
    # path('category/', CategoriesView.as_view()),
    # path('submition/', SubmitionsView.as_view()),
    path('category/', CategoryView.as_view()),
    path('login/', LoginView.as_view(), name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),


]