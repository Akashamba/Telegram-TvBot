import json
import requests


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_deets(name):
    deets = get_url("http://www.omdbapi.com/?apikey=56069cac&t="+name)
    js = json.loads(deets)
    return deets


get_deets("Contagion")