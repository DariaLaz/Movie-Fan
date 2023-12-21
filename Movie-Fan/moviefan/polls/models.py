from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=200)
    # image = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    rating = models.FloatField(default=0)
    genre = models.CharField(max_length=200, null=True, blank=True)
    year = models.IntegerField(default=0)
    director = models.CharField(max_length=200, null=True, blank=True)
    actors = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    duration = models.IntegerField(default=0)


class Category(models.Model):
    name = models.CharField(max_length=200)
    movies = models.CharField(max_length=200, null=True, blank=True)
    movies_id = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)


class Game(models.Model):
    name = models.CharField(max_length=200)
    categories = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    questions = models.CharField(max_length=200, null=True, blank=True)
    questions_id = models.CharField(max_length=200, null=True, blank=True)
    categories_id = models.CharField(max_length=200, null=True, blank=True)
    creator = models.CharField(max_length=200, null=True, blank=True)
    creator_id = models.CharField(max_length=200, null=True, blank=True)
    users = models.CharField(max_length=200, null=True, blank=True)
    users_id = models.CharField(max_length=200, null=True, blank=True)
    winner = models.CharField(max_length=200, null=True, blank=True)
    winner_id = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    is_started = models.BooleanField(default=False)
    is_waiting = models.BooleanField(default=False)
    is_ready = models.BooleanField(default=False)
    is_ready_to_start = models.BooleanField(default=False)
    is_ready_to_finish = models.BooleanField(default=False)


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    won_categories = models.CharField(max_length=200, null=True, blank=True)
    won_games_id = models.CharField(max_length=200, null=True, blank=True)
    won_categories_id = models.CharField(max_length=200, null=True, blank=True)

