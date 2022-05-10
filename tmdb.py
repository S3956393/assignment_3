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
    poster_url = get_movie_poster(movie_id, poster_path)

    return title, plot, poster_url

def get_movie_plot(movie_id):
    page = f"/movie/{movie_id}"
    parameters = {'api_key':API_SECRET_KEY, 'id':movie_id}
    movie_data = requests.get(BASE_URL + page, params=parameters).json()
    plot = movie_data['overview']

    return plot

def get_movie_poster(movie_id, poster_path):
    page = "/configuration"
    parameters = {'api_key':API_SECRET_KEY}
    image_data = requests.get(BASE_URL + page, params=parameters).json()['images']
 
    base_url = image_data['base_url']
    # This is a list. So please check beforehand for the sizes. 
    poster_sizes = image_data['poster_sizes']
    # Index 0 added for testing. Change as needed.
    poster_size = poster_sizes[0]
    image_url = base_url + poster_size + poster_path

    return image_url

def write_countries_to_file():
    '''Gets the available countries from the TMDB API and writing it to a CSV file'''
    # NOTE: This is missing one or two countries.
    page = "/configuration/countries"
    parameters = {'api_key':API_SECRET_KEY}
    countries = requests.get(BASE_URL + page, params=parameters).json()

    with open("countries.csv", "w") as f:
        for country in countries:
            f.write(str(country['iso_3166_1']) + "," + str(country['english_name']) + "\n")

# Run this function only once.
# write_countries_to_file()