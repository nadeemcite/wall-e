import requests

def get_from_url():
    url = "https://en.wikipedia.org/wiki/List_of_Bollywood_films_of_2018"
    r = requests.get(url)
    return r