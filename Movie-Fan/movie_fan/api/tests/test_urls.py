from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views.auth_views import LoginView, LogoutView, RegisterView
from ..views.sarp_views import MovieSarpView
from ..views.model_views.game_view import GameView
from ..views.model_views.category_view import CategoryView
from ..views.model_views.player_view import PlayersView
from ..views.model_views.join_game_view import JoinGameView
from ..views.model_views.score_view import ScoreView
from ..views.model_views.movie_view import MovieView
from ..views.model_views.submition_view import SubmitionView


class TestUrls(SimpleTestCase):

    def test_games_url_resolves(self):
        """Test games url resolves to the correct view function"""
        url = reverse('games')
        self.assertEqual(resolve(url).func.view_class, GameView)

    def test_game_url_resolves(self):
        """Test game url resolves to the correct view function"""
        url = reverse('game', args=[1])
        self.assertEqual(resolve(url).func.view_class, GameView)

    def test_players_url_resolves(self):
        """Test players url resolves to the correct view function"""
        url = reverse('players')
        self.assertEqual(resolve(url).func.view_class, PlayersView)

    def test_join_url_resolves(self):
        """Test join url resolves to the correct view function"""
        url = reverse('join')
        self.assertEqual(resolve(url).func.view_class, JoinGameView)

    def test_score_url_resolves(self):
        """Test score url resolves to the correct view function"""
        url = reverse('score')
        self.assertEqual(resolve(url).func.view_class, ScoreView)

    def test_categories_url_resolves(self):
        """Test categories url resolves to the correct view function"""
        url = reverse('categories')
        self.assertEqual(resolve(url).func.view_class, CategoryView)

    def test_category_url_resolves(self):
        """Test category url resolves to the correct view function"""
        url = reverse('category', args=[1])
        self.assertEqual(resolve(url).func.view_class, CategoryView)

    def test_login_url_resolves(self):
        """Test login url resolves to the correct view function"""
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, LoginView)

    def test_logout_url_resolves(self):
        """Test logout url resolves to the correct view function"""
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, LogoutView)

    def test_register_url_resolves(self):
        """Test register url resolves to the correct view function"""
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, RegisterView)

    def test_sarp_movie_url_resolves(self):
        """Test sarp_movie url resolves to the correct view function"""
        url = reverse('sarp_movie')
        self.assertEqual(resolve(url).func.view_class, MovieSarpView)

    def test_movies_url_resolves(self):
        """Test movies url resolves to the correct view function"""
        url = reverse('movies')
        self.assertEqual(resolve(url).func.view_class, MovieView)

    def test_submition_url_resolves(self):
        """Test submition url resolves to the correct view function"""
        url = reverse('submition')
        self.assertEqual(resolve(url).func.view_class, SubmitionView)
