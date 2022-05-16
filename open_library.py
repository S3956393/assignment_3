import requests, json

BASE_URL = "http://openlibrary.org"

def get_book_data_by_olid(olid):
    synopsis = ''
    image_url = ''
    page = "/works"
    resp = requests.get(BASE_URL + page + "/" + olid + ".json").json()
    # Check if there is a synopsis 
    if 'description' in resp:
        # Check if the synopsis is in the description or value key.
        if 'value' in resp['description']:
            synopsis = resp['description']['value']
        else: 
            synopsis = resp['description']
    # Check if there is a cover
    if 'covers' in resp:
        # resp['covers'] is a list, & since we don't know how many covers there are, use the first as default
        image_value = resp['covers'][0] 
        image_size = 'M' # Sizes: S, M, L
        image_url = f"https://covers.openlibrary.org/b/id/{image_value}-{image_size}.jpg"
        
    # cover_url = f"https://covers.openlibrary.org/b/olid/{olid}-M.jpg"

    return synopsis, image_url