from django.contrib import admin
from django.urls import path
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index),
    path('games/<int:gameId>', index),
    path('game/', index),
    path('movie/', index),
    path('create-game/', index),
    path('join/', index),
    path('register/', index),
    path('login/', index),
    path('upload/<int:categoryId>', index),
]