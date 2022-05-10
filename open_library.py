import requests

BASE_URL = "http://openlibrary.org/api"
JSCMD = "data"

def get_synopsis(work_id):
    page = "/works"
    URL = BASE_URL[:-4] + page + "/" + str(work_id) + ".json"
    resp = requests.get(URL).json()
    resp_as_list = list(resp['works'])[0]

    works_path = resp_as_list['key']
    synopsis_url =  BASE_URL[:-4] + works_path + ".json"
    synopsis_resp = requests.get(synopsis_url).json()
    synopsis = synopsis_resp['description']
    synopsis_without_link = synopsis.split("([source][1])", 1)[0]

    return synopsis_without_link

def get_book_data_by_isbn(isbn):
    page = "/books"
    parameters = {'bibkeys':f'ISBN:{isbn}', 'format':'json', 'jscmd':JSCMD}
    resp = requests.get(BASE_URL + page, params=parameters).json()
    book_data = list(resp.values())[0]

    title = book_data['title']
    author = book_data['authors']
    work_id = book_data['identifiers']['openlibrary'][0]
    synopsis = get_synopsis(work_id)
    # This is a dictionary with three sizes (which are the keys): small, medium, large 
    covers_dict = book_data['cover']
    # Change to the key needed
    cover = covers_dict['medium']

    return title, author, synopsis, cover