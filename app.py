from flask import Flask, render_template, get_template_attribute
import tmdb, open_library

app = Flask(__name__)

# NOTE: Only run this file directly.
# Copy the server when you run this file into your browswer
# You can either type in localhost:5000 or http://127.0.0.1:5000 (copied from the terminal)
# To end the server just press ctrl+c in the terminal

# This is the root/home page.
@app.route("/")
def home():
    # Replace the text in the string with the HTML file for the home page
    return render_template("enter_the_home_page.html")

@app.route("/map")
def map():
    pass
    # [ ] TODO: Get the ISO code from the front end, so we can get the
    # top movie from the TMDB API and the ISBN from the database

    # NOTE: No clue if this will work...
    # This method looks in the "the_map_page.html" (an example), and looks for
    # the isbn and region variables and passes their values to flask
    # isbn = get_template_attribute("map_test.html", isbn)
    # region = get_template_attribute("map_test.html", region)

    # movie_title, movie_plot, poster_url = tmdb.get_highest_grossing_movie(region)
    # book_title, author, excerpt, book_cover = open_library.get_book_data_by_isbn(isbn)

    # content = {
    #     'movie_title': movie_title,
    #     'movie_plot': movie_plot,
    #     'poster_url': poster_url,
    #     'book_title': book_title,
    #     'author': author,
    #     'excerpt': excerpt,
    #     'book_cover': book_cover
    # }

    # This renders the HTML page for variables in the content dictionary and passes it back to the HTML page
    # return render_template("map_test.html", **content)

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