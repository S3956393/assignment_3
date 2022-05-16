import requests

def get_cover(mbid):
    url = f"https://coverartarchive.org/release/{mbid}"
    resp = requests.get(url).json()
    images_data = list(resp['images'])
    cover_url = images_data[0]['thumbnails']['250']

    return cover_url