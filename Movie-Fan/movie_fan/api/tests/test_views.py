from django.test import TestCase, Client
from django.urls import reverse
from ..models import Game, Category, Player, Submition, Movie, PlayerScore
import json
from ..serializers.model_serializers import GameSerializer, CategorySerializer, PlayerSerializer, SubmitionSerializer, MovieSerializer  

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.games_url = reverse('games')
        self.game_url = reverse('game', kwargs={'game_id': '1'})
        self.categories_url = reverse('categories')
        self.category_url = reverse('category', kwargs={'category_id': '1'})
        self.players_url = reverse('players')   
        self.join_url = reverse('join')

        # self.score_url = reverse('score')   
        # self.login_url = reverse('login')
        # self.logout_url = reverse('logout')
        # self.register_url = reverse('register') 
        # self.sarp_movie_url = reverse('sarp_movie')
        # self.movies_url = reverse('movies')
        self.submition_url = reverse('submition')

        Game.objects.create( name='Game1', description='Game1 description', host='host1', code='code1')

        Category.objects.create(name='Category1', description='Category1 description', game_id='1')

        PlayerScore.objects.create()
        PlayerScore.objects.create()
        PlayerScore.objects.create()

        #not in the game
        Player.objects.create(name='player1', user_id='1', score=PlayerScore.objects.get(id=1))
        #in the game but hasnt submitted
        Player.objects.create(name='player2', user_id='2', score=PlayerScore.objects.get(id=2))
        #in the game and submitted
        Player.objects.create(name='player3', user_id='3', score=PlayerScore.objects.get(id=3))

        Movie.objects.create()

        Game.objects.get(id=1).add_player(Player.objects.get(id=2))
        Game.objects.get(id=1).add_player(Player.objects.get(id=3))

        Submition.objects.create(movie_id=1, category_id= 1, points=10, username='player2')

    def test_games_GET(self): 
        response = self.client.get(self.games_url)
        self.assertEqual(response.status_code, 200)

    def test_game_GET_correct(self):
        ...
        # response = self.client.get(self.game_url)
        # response = self.client.get(self.game_url, args=[1])
        
        # print(response.content)
        # json_data = json.loads(response.content)

        # game = Game.objects.get(id=1)
        # serializer = GameSerializer(game)

        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(json_data[0], serializer.data)

    def test_game_GET_incorrect(self):
        ...
    #     response = self.client.get(self.games_url, args=[2])
    #     print(response.content)
        # self.assertEqual(response.status_code, 404)

    def test_game_POST_correct(self):
        response = self.client.post(self.games_url, {
            'name': 'Game2',
            'description': 'Game2 description',
            'host': 'player1',
            'categories': [1]
        })

        json_data = json.loads(response.content)
        game = Game.objects.get(id=2)   
        serializer = GameSerializer(game)

        self.assertEqual(json_data, serializer.data)
        self.assertEqual(response.status_code, 201)

    def test_game_POST_incorrect(self):
        response = self.client.post(self.games_url, {
            'name': 'Game2',
            'description': 'Game2 description',
            'host': 'player1'
        })

        self.assertEqual(response.status_code, 400)

    def test_game_PUT_correct(self):
        ...
        # response = self.client.put(self.game_url, {
        #     'name': 'Game2',
        #     'description': 'Game2 description',
        #     'host': 'player1',
        #     'categories': [1]
        # })

        # json_data = json.loads(response.content)
        # game = Game.objects.get(id=1)   
        # serializer = GameSerializer(game)

        # self.assertEqual(json_data, serializer.data)
        # self.assertEqual(response.status_code, 200)

    def test_game_PUT_incorrect(self):
        ...
        # response = self.client.put(self.game_url, {
        #     'name': 'Game2',
        #     'description': 'Game2 description',
        #     'host': 'player1'
        # })

        # self.assertEqual(response.status_code, 400)

    def test_game_DELETE(self):
        ...
    #     response = self.client.delete(self.game_url)
    #     self.assertEqual(response.status_code, 204)
        
    def test_categories_GET(self):
        response = self.client.get(reverse('categories'))
        self.assertEqual(response.status_code, 200)

    def test_category_GET_correct(self):
        ...
        # response = self.client.get(self.category_url)
        # self.assertEqual(response.status_code, 200)
    
    def test_category_GET_incorrect(self):  
        ...
        # response = self.client.get(reverse('category', args=[2]))
        # self.assertEqual(response.status_code, 404)

    def test_category_POST_correct(self):  
        response = self.client.post(self.categories_url, {
            'name': 'Category3',
            'description': 'Category3 description'
        })

        json_data = json.loads(response.content)
        category = Category.objects.get(id=2)   
        serializer = CategorySerializer(category)

        self.assertEqual(json_data, serializer.data)
        self.assertEqual(response.status_code, 201)

    def test_category_POST_incorrect(self):
        ...
        # response = self.client.post(self.categories_url, {
        #     'nam1e': 'Category2',
        #     'description': 'Category2 description'
        # })
        # print(response.content)
         
        # self.assertEqual(response.status_code, 400)

    def test_category_PUT_correct(self):
        ...
        # response = self.client.put(self.category_url, {
        #     'name': 'Category2',
        #     'description': 'Category2 description'
        # })

        # json_data = json.loads(response.content)
        # category = Category.objects.get(id=1)   
        # serializer = CategorySerializer(category)

        # self.assertEqual(json_data, serializer.data)
        # self.assertEqual(response.status_code, 200)

    def test_category_PUT_incorrect(self):
        ...
        # response = self.client.put(self.category_url, {
        #     'nam1e': 'Category2',
        #     'description': 'Category2 description'
        # })

        # self.assertEqual(response.status_code, 400)   

    def test_category_DELETE(self):
        ...
        # response = self.client.delete(self.category_url)
        # self.assertEqual(response.status_code, 204)

    def test_players_GET(self):
        response = self.client.get(self.players_url)
        self.assertEqual(response.status_code, 200)

    def test_join_game(self):
        response = self.client.post(self.join_url, {
            'game_id': 1,
            'player_id': 1,
            'username': 'player1',
            'code': 'code1'
        })

        self.assertEqual(response.status_code, 200)

    def test_join_game_incorrect_code(self):
        response = self.client.post(self.join_url, {
            'game_id': 1,
            'player_id': 1,
            'username': 'player1',
            'code': 'code2'
        })

        self.assertEqual(response.status_code, 400)

    def test_join_game_incorrect_params(self):
        response = self.client.post(self.join_url, {
            'game_id': 1,
            'player_id': 1,
            'username': 'player1'
        })

        self.assertEqual(response.status_code, 400)

    def test_submition_POST_correct(self):
        response = self.client.post(self.submition_url, {
            'movie_id': 1,
            'category_id': 1,
            'points': 10,
            'username': 'player2'
        })
        self.assertEqual(response.status_code, 201)

    
    def test_submition_POST_incorrect(self):
        response = self.client.post(self.submition_url, {
            'movie_id': 1,
            'category_id': 1,
            'points': 10,
        })
        self.assertEqual(response.status_code, 400)

    def test_submitions_GET(self):
        response = self.client.get(self.submition_url)
        self.assertEqual(response.status_code, 200)

    def test_submition_GET_category_id_correct(self):
        
        ...


    
    