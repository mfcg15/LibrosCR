from _app.config.connection import connectToMySQL

class Autor:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO autores (nombre , created_at, updated_at) VALUES (%(nombre)s,NOW(),NOW());"
        return connectToMySQL('esquema_libros').query_db( query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM autores;"
        results = connectToMySQL('esquema_libros').query_db(query)
        autores = []
        for autor in results:
            autores.append(autor)
        return autores
    
    @classmethod
    def get_autor(cls,data):
        query = "SELECT * FROM autores where id = %(id)s;"
        results = connectToMySQL('esquema_libros').query_db(query,data)
        autor = []
        for i in results:
            autor.append(i)
        return autor

    @classmethod
    def get_autor_libro(cls,data):
        query = "SELECT titulo, numero_paginas FROM libros inner join favoritos on libros.id = favoritos.libro_id inner join autores on autores.id = favoritos.autor_id where autor_id = %(id)s;"
        results = connectToMySQL('esquema_libros').query_db(query,data)
        autorlibros = []
        for i in results:
            autorlibros.append(i)
        return autorlibros
    
    @classmethod
    def get_lack_autor(cls,data):
        query = "SELECT * FROM autores where autores.id not in (select favoritos.autor_id from favoritos where favoritos.libro_id = %(id)s);"
        results = connectToMySQL('esquema_libros').query_db(query,data)
        lacklautor = []
        for i in results:
            lacklautor.append(i)
        return lacklautor