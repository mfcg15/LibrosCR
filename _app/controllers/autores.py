from flask import render_template, request, redirect
from _app.models.libro import Libro
from _app.models.autor import Autor
from _app.models.favoritos import Favorito
from _app import app

@app.route("/")
def index():
    return redirect('/authors')

@app.route("/authors")
def newAutores():
    autores = Autor.get_all()
    return render_template('authors.html', all_autores = autores)

@app.route("/authors/<int:id>")
def author(id):
    idAuthor = id
    data = {
        "id": idAuthor
    }
    autor = Autor.get_autor(data)
    autorlibros = Autor.get_autor_libro(data)
    libros = Libro.get_lack_libro(data)
    return render_template('authorshow.html', autor = autor, autorlibro = autorlibros, libros = libros)

@app.route('/create_autor', methods=["POST"])
def authorNew():
    data = {
        "nombre": request.form["nombre"]
    }
    Autor.save(data)
    return redirect('/authors')

@app.route('/create_favoriteAB', methods=["POST"])
def favoriteNewAB():
    data = {
        "autor_id": int(request.form["autor_id"]),
        "libro_id": int(request.form["libro_id"])
    }
    Favorito.save(data)
    return redirect(f'/authors/{int(request.form["autor_id"])}')