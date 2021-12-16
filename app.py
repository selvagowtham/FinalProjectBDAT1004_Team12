from flask import Flask, redirect, url_for, render_template, request
from CloudAPI import getMovieDetails
import FirebaseOperations

# Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret'


@app.route("/")
def index():
    return redirect(url_for('contacts'))


@app.route("/edit_contact/<id>", methods=('GET', 'POST'))
def edit_contact(id):
    movie = FirebaseOperations.getMovie(id)
    return render_template('web/edit_contact.html', movie=movie, key=id)


@app.route("/contacts")
def contacts():
    listMovies = FirebaseOperations.listMovies()
    return render_template('web/view_contacts.html', listMovies=listMovies)


@app.route("/search")
def search():
    name_search = request.args.get('name')
    movieDetails = getMovieDetails(name_search)
    print(movieDetails)
    if len(movieDetails) <= 0:
        return 'Sorry Movie not found pls try again'
    else:
        return render_template('web/contacts.html', contacts=movieDetails)


@app.route("/insert/movie", methods=('POST',))
def insert_movie():
    data = {
        'id': request.form['id'],
        'movie': request.form['name'],
        'image': request.form['image'],
        'description': request.form['description'],
    }

    FirebaseOperations.insertMovie(data)
    return redirect(url_for('contacts'))


@app.route("/update/movie", methods=('POST',))
def update_movie():
    FirebaseOperations.updateMovie(request.form['name'], request.form['id'],
                                   request.form['description'], request.form['image'],
                                   request.form['key'])
    return redirect(url_for('contacts'))


@app.route("/contacts/delete", methods=('POST',))
def contacts_delete():
    print(FirebaseOperations.deleteMovie(request.form['id']))
    return redirect(url_for('contacts'))


if __name__ == "__main__":
    app.run(debug=True)
