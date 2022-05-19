from flask import Flask, render_template, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from markupsafe import Markup
import tmdb, open_library, music_brainz, os, boto3

s3 = boto3.client('s3')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/IIT_assigment_3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Author(db.Model):
    __tablename__ = 'author'
    author_id = db.Column(db.Integer, primary_key=True, nullable=False)
    author_name = db.Column(db.String, nullable=False)
    ol_id = db.Column(db.String, db.ForeignKey('book.ol_id'), nullable=False)

class Book(db.Model):
    __tablename__ = 'book'
    ol_id = db.Column(db.String, primary_key=True, nullable=False)
    book_title = db.Column(db.String, nullable=False)
    iso_code = db.Column(db.String(2), db.ForeignKey('country.iso_code'), nullable=False)

class Song(db.Model):
    __tablename__ = 'song'
    mbid = db.Column(db.String(36), primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    iso_code = db.Column(db.String(2), db.ForeignKey('country.iso_code'), nullable=False)

class Singer(db.Model):
    __tablename__ = 'singer'
    singer_id = db.Column(db.Integer, primary_key=True, nullable=False)
    singer_name = db.Column(db.String, nullable=True)
    mbid = db.Column(db.String(36), db.ForeignKey('song.mbid'), nullable=False)

class Country(db.Model):
    __tablename__ = 'country'
    iso_code = db.Column(db.String(2), primary_key=True, nullable=False)
    country_name = db.Column(db.String, nullable=False)

def get_book_data(iso):
    country = Country.query.filter_by(iso_code=iso).first()
    country_name = country.country_name

    book = Book.query.filter_by(iso_code=iso).first()
    book_title = book.book_title
    olid = book.ol_id

    author = Author.query.filter_by(ol_id=olid).first()
    author_name = author.author_name

    return country_name, book_title, author_name, olid

def get_song_data(iso):
    song = Song.query.filter_by(iso_code=iso).first()
    song_title = song.title
    mbid = song.mbid

    singer = Singer.query.filter_by(mbid=mbid).first()
    singer_name = singer.singer_name

    return song_title, singer_name, mbid

@app.route("/")
def home():
    svg_map = s3.generate_signed_url('get_object',
                                                    Params={'Bucket': 'iit-group12',
                                                            'Key': 'World map with configurable borders.svg'},
                                                    ExpiresIn=3600)
    # svg_map = s3.download_fileobj('iit-group12', 'World map with configurable borders.svg')
    #  open("http://s3.amazonaws.com/iit-group12/").read()
    return render_template("map.html", svg_map=Markup(svg_map))

@app.route("/get_iso_code", methods = ['POST'])
def get_iso_code():
    if request.method == 'POST':
        iso_code = request.get_json()['isoCode']

        if len(iso_code) == 2:
            movie_title, movie_plot, movie_poster_url = tmdb.get_highest_grossing_movie(iso_code)
            country, book_title, author, olid = get_book_data(iso_code)
            book_synopsis, book_cover = open_library.get_book_data_by_olid(olid)
            song_title, singer, mbid = get_song_data(iso_code)
            album_cover = music_brainz.get_cover(mbid)

            contents = {
                'country': country,
                'movie_title': movie_title,
                'movie_plot': movie_plot,
                'movie_poster': movie_poster_url,
                'book_title': book_title,
                'author': author,
                'book_synopsis': book_synopsis,
                'book_cover': book_cover,
                'song_title': song_title,
                'singer': singer,
                'album_cover': album_cover
            }


            return jsonify('', render_template('get_iso_code.html', **contents))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port, threaded=True)