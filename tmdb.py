import requests, os

API_SECRET_KEY = os.environ.get("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

def get_highest_grossing_movie(region):
    page = "/discover/movie"
    parameters = {'api_key':API_SECRET_KEY, 'region':region, 'sort_by':'revenue.desc'}

    films = requests.get(BASE_URL + page, params=parameters).json()['results']
    highest_grossing_film = films[0]

    title = highest_grossing_film['title']
    poster_path = highest_grossing_film['poster_path']
    movie_id = highest_grossing_film['id']
    plot = get_movie_plot(movie_id)
    poster_url = get_movie_poster(poster_path)
        
    return title, plot, poster_url

def get_movie_plot(movie_id):
    page = f"/movie/{movie_id}"
    parameters = {'api_key':API_SECRET_KEY, 'id':movie_id}
    movie_data = requests.get(BASE_URL + page, params=parameters).json()
    plot = movie_data['overview']

    return plot

def get_movie_poster(poster_path):
    page = "/configuration"
    parameters = {'api_key':API_SECRET_KEY}
    image_data = requests.get(BASE_URL + page, params=parameters).json()['images']
 
    base_url = image_data['secure_base_url']
    poster_sizes = image_data['poster_sizes'] # This is a list set the image
    poster_size = poster_sizes[1]
    image_url = base_url + poster_size + poster_path

    return image_url