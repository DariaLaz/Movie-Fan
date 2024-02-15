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
    results = models.JSONField(default=dict)


    def start(self):
        self.mode = 1
        self.save()

    def finish(self):
        self.mode = 2

        sortedRes  = sorted(self.results.items(), key=lambda x:x[1], reverse=True)
        self.results  = dict(sortedRes)    

        i = 1
        for key in self.results:
            player = Player.objects.get(name=key)
            player.update_score(i)
            i += 1
            if i > 3:
                break

        self.save()

    def add_player(self, player):
        self.participants.add(player)
        self.results[player.name] = 0
        self.save()

    def update_results(self, player, points):
        if not player.name in self.results:
            self.results[player.name] = 0
        self.results[player.name] += int(points)
        self.save()

    def num_of_players(self):
        return self.participants.count()

    def unlock_next_categories(self):
        categories = self.categories.all()
        for category in categories:
            if category.mode == 0:
                category.mode = 1
                category.save()
                return True
        return False
    
    def lock_curr_categories(self):
        categories = self.categories.all()
        for category in categories:
            if category.mode == 1:
                category.mode = 2
                category.save()
                return True
        return False
    

    def __str__(self):
        return self.name
    
class PlayerScore(models.Model):
    first_place = models.IntegerField(default=0)
    second_place = models.IntegerField(default=0)
    third_place = models.IntegerField(default=0)
    all_games = models.IntegerField(default=0)
    created = models.IntegerField(default=0)

    def add_first(self):
        self.first_place += 1

class Player(models.Model):
    user_id = models.CharField(max_length=50, unique=True, default='')
    name = models.CharField(max_length=50, unique=True)
    my_games = models.ManyToManyField('Game', related_name='players', default=set)
    score = models.ForeignKey(PlayerScore, on_delete=models.CASCADE, null=True)

    def add_first(self):
        self.score.add_first()

    def update_created(self):
        if self.score is None:
            self.score = PlayerScore.objects.create()
        self.score.created += 1
        self.score.save()
    def update_score(self, place=0):
        if self.score is None:
            self.score = PlayerScore.objects.create()
        if place == 1:
            self.score.first_place += 1
        elif place == 2:
            self.score.second_place += 1
        elif place == 3:
            self.score.third_place += 1
        self.score.all_games += 1
        self.score.save()

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    submitions = models.ManyToManyField('Submition', related_name='categories')
    game_id = models.IntegerField(default=0)
    voters = models.ManyToManyField('Player', default=set)
    mode = models.IntegerField(default=0) # 0 - not started yet, 1 - in progress uploading, 2 - in progress voting, 3 - finished 

    def num_of_votes(self):
        return self.voters.count()

    def has_voted(self, player):
        return self.voters.filter(id=player.id).exists()
    
    def add_voter(self, player):
        self.voters.add(player)
        self.save()

    def start_uploading(self):
        self.mode = 1
        self.save()

    def start_voting(self):
        self.mode = 2
        self.save()

    def finish(self):
        self.mode = 3
        self.save()

    def add_submition(self, submition):
        self.submitions.add(submition)
        self.save()

    def num_of_submitions(self):
        return self.submitions.count()

    def get_results(self):
        submitions = self.submitions.all()
        results = {}
        for submition in submitions:
            if submition.movie.title not in results:
                results[submition.movie.title] = 0
            results[submition.movie.title] += submition.points
        return results
    
    def get_submitions(self):
        return self.submitions
    
    def has_submition(self, player):
        return self.submitions.filter(player=player).exists()

    def __str__(self):
        return self.name

class Submition(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def add_points(self, points):
        self.points += int(points)
        
        self.save()

    def __str__(self):
        return str(self.__getattribute__("id"))

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField(default=0)
    link = models.CharField(max_length=300 ,default='')
    genre = models.CharField(max_length=50) #category in sarpApi
    tumbnail = models.CharField(max_length=300)

    def __str__(self):
        return self.title

