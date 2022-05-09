from flask import Flask, render_template
import tmdb

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
    # TODO: Somehow we need to get JavaScript? to pass the ISO code from the map
    # so that we can get the movie via the TMDB API for that country

    # NOTE: Uncomment the line of 22 and 25 when the above is done, and delete line 26
    # title, plot, poster_url = tmdb.get_highest_grossing_movie(region)
    # This renders the HTML page for the map, and passes the title, plot and poster url back to the HTML page

    # return render_template("the_map_page.html", title=title, plot=plot, poster_url=poster_url)
    return "This is the map page"

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