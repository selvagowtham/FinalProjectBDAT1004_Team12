from firebase import firebase

firebaseUrl = 'https://cloudapifirebasedb-5056f-default-rtdb.firebaseio.com/'
firebaseClient = firebase.FirebaseApplication(firebaseUrl, None)
dbName = 'cloudapifirebasedb-5056f'
tableName = 'Movies'
path = '/' + dbName + '/' + tableName + '/'


def insertMovie(movie):
    result = firebaseClient.post(path, movie)
    print(result)

def getMovie(key):
    result = firebaseClient.get(path+"/"+key, '')
    return result

def listMovies():
    result = firebaseClient.get(path, '')
    return result


def deleteMovie(key):
    result = firebaseClient.delete(path, key)
    return result


def updateMovie(name, id, description, image, key):
    firebaseClient.put(path + '/' + key, 'movie', name)
    firebaseClient.put(path + '/' + key, 'id', id)
    firebaseClient.put(path + '/' + key, 'description', description)
    result = firebaseClient.put(path + '/' + key, 'image', image)
    return result

