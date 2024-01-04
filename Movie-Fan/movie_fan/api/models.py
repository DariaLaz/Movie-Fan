from django.db import models
import random
import string

def generate_code_for_game():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if not Game.objects.filter(code=code).exists():
            break
    return code



class Game(models.Model):
    code = models.CharField(max_length=6, default=generate_code_for_game, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    host = models.CharField(max_length=50, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField('Player', related_name='games')
    categories = models.ManyToManyField('Category', related_name='games')
    mode = models.IntegerField(default=0) # 0 - waiting for players, 1 - in progress, 2 - finished

    def get_results(self):
        submitions = Submition.objects.filter(game=self)
        results = {}
        for submition in submitions:
            if submition.player.name not in results:
                results[submition.player.name] = 0
            results[submition.player.name] += submition.points
        return results

    def __str__(self):
        return self.name
    
class PlayerScore(models.Model):
    first_place = models.IntegerField(default=0)
    second_place = models.IntegerField(default=0)
    third_place = models.IntegerField(default=0)
    all_games = models.IntegerField(default=0)

class Player(models.Model):
    name = models.CharField(max_length=50, unique=True)
    my_games = models.ManyToManyField('Game', related_name='players')
    score = models.ForeignKey(PlayerScore, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    submitions = models.ManyToManyField('Submition', related_name='categories')

    def __str__(self):
        return self.name

class Submition(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    tumbnail = models.CharField(max_length=100)

    def __str__(self):
        return self.title

