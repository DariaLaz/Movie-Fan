
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Game, Category, Movie, Player, PlayerScore, Submition

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.game = Game.objects.create(name='testgame', description='testdescription', host=self.user)
        self.category = Category.objects.create(name='testcategory', description='testdescription')
        self.movie = Movie.objects.create(title='testmovie', description='testdescription', rating=5, genre='testgenre', tumbnail='testtumbnail', link='testlink')
        self.player = Player.objects.create(name='testplayer')
        self.playerscore = PlayerScore.objects.create()
        self.submition = Submition.objects.create(player=self.player, category=self.category, movie=self.movie)

    def test_game_model(self):
        self.assertEqual(self.game.name, 'testgame')
        self.assertEqual(self.game.description, 'testdescription')
        self.assertEqual(self.game.host, self.user)

    def test_category_model(self):
        self.assertEqual(self.category.name, 'testcategory')
        self.assertEqual(self.category.description, 'testdescription')

    def test_movie_model(self):
        self.assertEqual(self.movie.title, 'testmovie')
        self.assertEqual(self.movie.description, 'testdescription')
        self.assertEqual(self.movie.rating, 5)
        self.assertEqual(self.movie.genre, 'testgenre')
        self.assertEqual(self.movie.tumbnail, 'testtumbnail')
        self.assertEqual(self.movie.link, 'testlink')   

    def test_player_model(self):
        self.assertEqual(self.player.name, 'testplayer')

    def test_submition_model(self):
        self.assertEqual(self.submition.player, self.player)
        self.assertEqual(self.submition.category, self.category)
        self.assertEqual(self.submition.movie, self.movie)