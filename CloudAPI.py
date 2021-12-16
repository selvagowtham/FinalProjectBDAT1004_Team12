# import imdb
#
# moviesDB = imdb.IMDb()
#
# # # Help?

import ast
import requests

IMDB_Key = "k_cjax3vz6"

def getMovieDetails(movieName):
    r = requests.get('https://imdb-api.com/en/API/SearchMovie/' + IMDB_Key + '/' + movieName)
    resp = ast.literal_eval(r.text)
    return resp['results']

