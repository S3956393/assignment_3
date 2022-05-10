import requests

BASE_URL = "http://openlibrary.org/api/books"
JSCMD = "data"

def get_book_data_by_isbn(isbn):
    parameters = {'bibkeys':f'ISBN:{isbn}', 'format':'json', 'jscmd':JSCMD}
    book_data = requests.get(BASE_URL, params=parameters).json()
    book_data_list = list(book_data.values())[0]

    title = book_data_list['title']
    author = book_data_list['authors']
    excerpt = book_data_list['excerpts'][0]['text']
    # This is a dictionary with three sizes (which are the keys): small, medium, large 
    covers_dict = book_data_list['cover']
    # Change to the key needed
    cover = covers_dict['medium']

    return title, author, excerpt, cover