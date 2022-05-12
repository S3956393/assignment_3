from pickle import NONE
from flask import Flask, render_template, get_template_attribute, url_for, request, jsonify
from markupsafe import Markup
import tmdb, open_library

app = Flask(__name__)

# NOTE: Only run this file directly.
# Copy the server when you run this file into your browswer
# You can either type in localhost:5000 or http://127.0.0.1:5000 (copied from the terminal)
# To end the server just press ctrl+c in the terminal

@app.route("/")
def home():
    svg_map = open("static\images\World map with configurable borders.svg").read()
    return render_template("map.html", svg_map=Markup(svg_map))

@app.route("/get_iso_code", methods = ['POST'])
def get_iso_code():
    if request.method == 'POST':
        res = request.get_data()
        iso_code = res.decode('utf-8')[-2:]

        movie_title, movie_plot, poster_url = tmdb.get_highest_grossing_movie(iso_code)
        content = {
            'movie_title': movie_title,
            'movie_plot': movie_plot,
            'poster_url': poster_url
        }
    return jsonify('', render_template('get_iso_code.html', **content))

# Template for adding subpages
# Change the '/some-page' to something relevant. 
# Since we don't have a navigation bar yet, just type localhost:5000/some_page in the search bar AFTER you run this file. 
@app.route("/some_page")
# Similarly, change the function name to something relevant for understandability
def some_page():
    # Change the text in the string to the HTML file for the page, which needs to be in the templates folder.
    return render_template("some_page.html")

if __name__ == "__main__":
    app.run(debug=True)