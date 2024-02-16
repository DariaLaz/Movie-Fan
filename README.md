# Movie-Fan

## Description
Movie Fan is a web application that allows users to create and join games. Each game has a set of categories. 
After the game is created, the host can invite friends to join the game by unique code. The game can only be started or deleted by the host. 
The game will display a list of categories and the user will have to select a movie from each category. At each moment only one category is active either for uploaing a movie or for voting.
Once all participants have uploaded their movies in the category, the game will display the movies that have been uploaded and each user will have to vote spreading 10 points between the movies (downvotes allowed).
The game will display the results and the winner of the category. The game will continue until all categories have been played. The user with the most points at the end of the game will be the winner.

#### Frontend Documentation
##### Overview
The frontend of the application is built using React. react-router-dom is used for routing and navigation.

##### Routes
- ````/```` - Home page
- ````/login```` - Login page
- ````/register```` - Register page
- ````/games/:id```` - Game details page
- ````/upload/:category_id```` - Upload movie page
- ````/vote/:category_id```` - Vote page
- ````/join```` - Join game page
- ````/create-game```` - Create game page

##### Components
- Home
- Login
- Register
- GameDetails
- UploadMovie
- Vote
- JoinGame
- CreateGame

#### Backend Documentation
##### Overview
The backend of the application is built Django and Django Rest Framework.

##### Models
```python
- Game
    - code: String
    - name: String
    - description: String
    - host: String
    - created_at: Date
    - participants: [Player]
    - categories: [Category]
    - mode: Integer
    - results: JSON

- Player
    - user_id: String
    - name: String
    - my_games: [Game]
    - score: PlayerScore

- PlayerScore
    - first_place: Integer
    - second_place: Integer
    - third_place: Integer
    - all_games: Integer
    - created: Integer

- Category
    - name: String
    - description: String
    - submitions: [Submition]
    - game_id: Integer
    - voters: [Player]
    - mode: Integer

- Submition
    - player: Player
    - movie: Movie
    - category: Category
    - points: Integer

- Movie
    - title: String
    - description: String
    - rating: Float
    - link: String
    - genre: String
    - tumbnail: String
```

##### Routes

- ````GET /games/```` - Get all games
- ````POST /games/ ````- Create a new game
    required fields in body: name, description, host, categories
- ````GET /games/:id```` - Get a game by id
- ````PUT /games/:id```` - Update a game by id
- ````DELETE /games/:id```` - Delete a game by id
- ````GET /players/````
    if player_id is provided in query, get a player by id
    if name is provided in query, get a player by name
    if no query is provided, get all players
- ````POST /players/```` - Create a new player
    required fields in body: name
- ````GET /categories/ ````
    if category_id is provided in query, get a category by id
    if no query is provided, get all categories
- ````POST /categories/```` - Create a new category
    required fields in body: name, description
- ````DELETE /category/```` - Delete a category by id
- ````GET /movies/ ````
    if movie_id is provided in query, get a movie by id
    if no query is provided, get all movies
- ````POST /movies/```` - Create a new movie
    required fields in body: title, description, rating, link, genre, tumbnail
- ````GET /submitions/```` 
    if submition_id is provided in query, get a submition by id
    if category_id is provided in query, get all submitions by category
    if no query is provided, get all submitions
- ````POST /submitions/```` - Create a new submition
    required fields in body: username, movie_id, category_id
- ````POST /join/```` - Create a new join
    required fields in body: code, username
- ````GET /score/ ````
    if player_id is provided in query, get a score by player id
    if no query is provided, get all scores
- ````POST /login/```` - Login
    required fields in body: username, password
- ````POST /logout/```` - Logout
- ````POST /register/```` - Register
    required fields in body: email, username, password
- ````GET /sarp_movie/ ````
    if q is provided in query, get a movie by title
    if no query is provided, get empty list

##### Serializers'
- GameSerializer
- PlayerSerializer
- PlayerScoreSerializer
- CategorySerializer
- SubmitionSerializer
- MovieSerializer
- VoteSerializer
- JoinSerializer
- ScoreSerializer
- SarpMovieSerializer
- CategorySerializer

##### Views
- GameView
- PlayerView
- PlayerScoreView
- CategoryView
- SubmitionView
- MovieView
- VoteView
- JoinView
- ScoreView
- SarpMovieView
- CategoryView
- LoginView
- LogoutView
- RegisterView

#### Third Party Services
- The application uses SARP Movie Database API for fetching movie data. 
