import json
import requests

def get_deets(name):
    deets = get_url("http://www.omdbapi.com/?apikey=56069cac&t="+name)
    js = json.loads(deets)
    return js


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_str(movie):
    l = []
    for i in range(len(movie)):
        l.append(str(list(movie.keys())[i]) + " : " + str(movie[list(movie.keys())[i]]))

    st = ""
    for i in range(len(l)):
        st = st + l[i] + "\n"
    return st


print(get_str(get_deets("Contagion")))
