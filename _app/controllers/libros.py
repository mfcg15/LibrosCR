from flask import render_template, request, redirect
from _app.models.libro import Libro
from _app.models.autor import Autor
from _app.models.favoritos import Favorito
from _app import app


@app.route("/books")
def books():
    libros = Libro.get_all()
    return render_template('books.html', all_libros = libros)

@app.route("/books/<int:id>")
def book(id):
    idBook = id
    data = {
        "id": idBook
    }
    book = Libro.get_libro(data)
    libroautor = Libro.get_libro_autor(data)
    autores = Autor.get_lack_autor(data)
    return render_template('bookshow.html', book = book, autores = autores, libroautor = libroautor)


@app.route('/create_book', methods=["POST"])
def bookNew():
    data = {
        "titulo": request.form["titulo"],
        "numero_paginas" : request.form["numero_paginas"]
    }
    Libro.save(data)
    return redirect('/books')

@app.route('/create_favoriteBA', methods=["POST"])
def favoriteNewBA():
    data = {
        "autor_id": int(request.form["autor_id"]),
        "libro_id": int(request.form["libro_id"])
    }
    Favorito.save(data)
    return redirect(f'/books/{int(request.form["libro_id"])}')